from src import app
from flask import render_template, url_for, flash, redirect
from src.forms import RegistrationForm, LoginForm
from src.models import User

# posts = [
#     {
#         'author': 'Kamran Karimov',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'March 29 2021'
#     },
#     {
#         'author': "John Doe",
#         "title": "Blog Post 2",
#         "content": "Second post content",
#         "date_posted": "March 29 2021"
#     }
# ]


@app.route('/')
@app.route('/home')
def home():
    # products_api = main('ultrawide monitor')
    return render_template('home.html')


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