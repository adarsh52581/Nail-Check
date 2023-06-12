from flask import Blueprint, render_template 
from flask_bootstrap import Bootstrap

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/UpAndPredict')
def Up_Predict():
    return render_template("Up&Predict.html")

