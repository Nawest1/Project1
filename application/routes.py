from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.forms import AddPortfolio, AddStock,UpdatePortfolio
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
    portfolio = Portfolio.query.all()
    stocks = Stock.query.all()
    #portfolio = Portfolio.query.all()
    #stocks = Stock.query.all()
    #holdings=db.session.query(Portfolio,Stock).distinct(Portfolio.id)
    return render_template("viewportfolio.html", portfolio=portfolio, stocks=stocks)


@app.route('/delete/<portfolio>', methods=['GET', 'POST'])
def delete(portfolio):
    portfolio = Portfolio.query.filter_by(name=portfolio).first()
    db.session.delete(portfolio)
    db.session.commit()
    return redirect(url_for('view_portfolio'))

@app.route('/update/<portfolio>', methods=['GET','POST'])
def update_portfolio(portfolio):
    form = UpdatePortfolio()
    portfolio = Portfolio.query.filter_by(name=portfolio).first()
    portfolio_id = portfolio.id
    stocks= Stock.query.all()
    for stock in portfolio.stocks:
        form.stock.choices.append(stock.stock)
    if request.method == 'POST':
        newposition = form.newposition.data
        stock.position = newposition
        db.session.commit()
        return redirect(url_for('view_portfolio'))
    return render_template("update_portfolio.html", form=form)



    




    