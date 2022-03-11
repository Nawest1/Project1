from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


class AddPortfolio(FlaskForm):
    portfolio_name = StringField('Portfolio Name', validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField('Add Portfolio Name')

class AddStock(FlaskForm):
    newstock = StringField('Stock Name', validators=[DataRequired(message="This field cannot be left blank")])
    newposition = IntegerField('Number of shares')
    portfolio = SelectField('Add to portfolio:', choices=[])
    submit = SubmitField('Add Stock')

class UpdatePortfolio(FlaskForm):
    stock = SelectField('Update Position:', choices=[])
    newposition = IntegerField('Number of shares')
    submit = SubmitField('Change Position Size')