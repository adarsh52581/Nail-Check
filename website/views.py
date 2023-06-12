from flask import Blueprint, render_template 
from flask_bootstrap import Bootstrap

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

