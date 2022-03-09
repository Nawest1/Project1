from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.forms import AddPortfolio, AddStock #ViewPortfolio
from application.models import Portfolio, Stock

@app.route("/")
def homePage():
    return render_template("layout.html")

@app.route('/add-portfolio', methods=['GET', 'POST'])
def add_portfolio():
    form = AddPortfolio()
    if request.method == 'POST':
        portfolio_name = form.portfolio_name.data
        portfolio = Portfolio(name = portfolio_name)
        db.session.add(portfolio)
        db.session.commit()
        return redirect(url_for('add_stock'))
    return render_template("add_portfolio.html", form=form)

@app.route('/add-stockholding', methods=['GET','POST'])
def add_stock():
    form = AddStock()
    portfolios = Portfolio.query.all()
    for portfolio in portfolios:
        form.portfolio.choices.append((portfolio.id, portfolio.name))
    if request.method == 'POST':
        newstock = form.newstock.data
        newposition = form.newposition.data
        portfolio_id = form.portfolio.data
        newstockholding = Stock(stock = newstock, position = newposition, portfolio_id = portfolio_id)
        db.session.add(newstockholding)
        db.session.commit()
        #return redirect(url_for('add_o', qid=newquest.id))
    return render_template("add_stock.html", form=form)


@app.route('/view-holdings', methods=['GET', 'POST'])
def view_portfolio():
    portfoliohld = Portfolio.query.all
    for portfolios in portfoliohld:
        portfolio = Portfolio.name
        stocks = Portfolio.stock.stock
    return portfolio, stocks
    #portfolio = Portfolio.query.all()
    #stocks = Stock.query.all()
    #holdings=db.session.query(Portfolio,Stock).distinct(Portfolio.id)
    return render_template("viewportfolio.html", portfolio=portfolio, stocks=stocks)
    #for portfolio in portfolios:
        #form.portfolio.choices.append((portfolio.id, portfolio.name))
        #portfolio_id=form.portfolio.data
    #portfolio_ids = form.portfolio.data
    #portfolio_name = Portfolio.query.filter_by(id=portfolio)
       # stockholdings = Stock.query.filter_by(portfolio_id=portfolio_id)
    #portfolioholding = stockholdings
    #return render_template("viewportfolio.html", form=form, portfolio=portfolio,)






    