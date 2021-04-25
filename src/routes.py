from src import app
from flask import render_template, url_for, flash, redirect
from src.forms import *
from src.amazon_scrape import *
from src.tapaz_scrape import *
from src.aliexpress_scrape import *


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    item = form.item.data
    if item:
        amazon_product = amazon_scraper(item)
        tapaz_product = tapaz_scraper(item)
        aliexpress_product = aliexpress_scraper(item)
    else:
        amazon_product = {}
        tapaz_product = {}
        aliexpress_product = {}
    return render_template('home.html', title='Search', form=form) # , aliexpress_product=aliexpress_product) # amazon_product=amazon_product, tapaz_product=tapaz_product, )


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in successfully', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)