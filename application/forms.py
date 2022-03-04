class AddPortfolio(FlaskForm):
    portfolio_name = StringField('Portfolio Name', validators=[DataRequired(message="This field cannot be left blank")])
    submit = SubmitField('Add Portfolio Name')

class AddStock(FlaskForm):
    newstock = StringField('Stock Name', validators=[DataRequired(message="This field cannot be left blank")])
    newposition = IntegerField('Number of shares')
    portfolio = SelectField('Add to portfolio:', choices=[])
    submit = SubmitField('Add Stock')