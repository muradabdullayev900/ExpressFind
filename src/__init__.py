from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from amazon_scrape import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '305e2c4a398c87c734c234c395c2aa46'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from src import routes