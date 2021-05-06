from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '305e2c4a398c87c734c234c395c2aa46'

from src import routes
