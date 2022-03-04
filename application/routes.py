from flask import Flask, render_template, request, redirect
from application import app, db
#from application.forms import AddUser, CustomerLogin, AddBooking, UpdateBooking, UpdateAccount, AdminLogin
from application.models import Portfolio, Stock

@app.route("/")
def homePage():
    return render_template("layout.html")