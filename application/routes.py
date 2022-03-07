from flask import Flask, render_template, request, redirect, url_for
from application import app, db
from application.forms import AddPortfolio, AddStock
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


    @app.route('/view-holdings', methods=['GET','POST'])
def view_portfolio():
    form = ViewPortfolio()
    portfolios = Portfolio.query.all()
    for portfolio in portfolios:
        form.portfolio.choices.append((portfolio.id, portfolio.name))
    if request.method == 'POST':
        portfolio_id = form.portfolio.data
        stockholdings = Stock.query.all(stock.portfolio_id=portfolio.id.)
        db.session.add(stockholdings)
        db.session.commit()
    return render_template("viewportfolio.html", form=form, portfolio_id=portfolio_id, stockholdings=stockholdings)






    question = Questions.query.filter_by(quiz_id=qid, num=qnum).first()
    options = question.options
    for option in options:
        form.sel_opt.choices.append((option.id, option.option))
    if request.method == 'POST':
        ans_opt = form.sel_opt.data
        ans = Options.query.filter_by(id = ans_opt).first()
        newans = Answer(name = ans.__str__(), status = ans.status)
        db.session.add(newans)
        db.session.commit()
        if qnum == Questions.query.filter_by(quiz_id=qid).order_by(Questions.num.desc()).first().num:
            return redirect(url_for('show_results'))
        else:
            return redirect(url_for('answer_q', qid=qid, qnum=qnum + 1))
    return render_template('answer-question.html', form=form, question=question, options=options)