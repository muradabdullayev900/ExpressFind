from src import app
from flask import render_template, request
from src.forms import SearchForm
from src.amazon_filter import AmazonFilter
from src.tapaz_filter import TapazFilter
from src.aliexpress_filter import AliexpressFilter

amazon_filter = AmazonFilter()
tapaz_filter = TapazFilter()
aliexpress_filter = AliexpressFilter()

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    amazon_product = []
    tapaz_product = []
    aliexpress_product = []
    form = SearchForm()
    item = form.item.data
    min_price = form.min_price.data
    max_price = form.max_price.data
    if request.method == 'POST':
        sort = request.form['sort']
        currency = request.form['currency']
        amazon = request.form.getlist('amazon')
        tapaz = request.form.getlist('tapaz')
        aliexpress = request.form.getlist('aliexpress')
        if amazon:
            amazon_product = amazon_filter.Filter(item, sort, currency, min_price, max_price)
        if tapaz:
            tapaz_product = tapaz_filter.Filter(item, sort, currency, min_price, max_price)
        if aliexpress:
            aliexpress_product = aliexpress_filter.Filter(item, sort, currency, min_price, max_price)

        return render_template('home.html', title='Search', form=form, amazon_product=amazon_product, tapaz_product=tapaz_product, aliexpress_product=aliexpress_product)
    else:
        return render_template('home.html', title='Search', form=form, amazon_product=amazon_product, tapaz_product=tapaz_product, aliexpress_product=aliexpress_product) # , aliexpress_product=aliexpress_product) # amazon_product=amazon_product, tapaz_product=tapaz_product, )


@app.route('/about')
def about():
    return render_template('about.html', title="About")
