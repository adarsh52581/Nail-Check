from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        name= request.form.get('name')
        email= request.form.get('email')
        password= request.form.get('password')
        password2= request.form.get('password2')
        if password != password2:
            flash('Passwords do not match!', category='error')
        else:
            flash('Account created successfully!', category='success')
        print(name,email,password)
    return render_template("sign-up.html")