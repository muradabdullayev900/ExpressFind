from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    item = StringField('Item Search', validators=[DataRequired()])
    min_price = FloatField('Minimum Price')
    max_price = FloatField('Maximum Price')
    submit = SubmitField('Search')
