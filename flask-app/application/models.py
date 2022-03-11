from application import db

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), nullable=False)
    stocks = db.relationship ('Stock', backref='portfolio',lazy='dynamic')

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))
    stock = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Integer, nullable=False)