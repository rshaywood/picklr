from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session, render_template, redirect, request
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
bcrypt = Bcrypt(app)

# CREATE

@app.route('/user/register')
def show_registration_form():
    return render_template('register.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    new_user = User.create_user(request.form)
    if new_user:
        return redirect('/dashboard')
    return redirect('/')


# READ

@app.route('/')
def landing_page():
    return render_template('landing_page.html')
def login():
    if User.login(request.form):
        return redirect('/dashboard')
    return redirect('/')

# LOGiIN/OUT - ROUTES

# @app.route('/', methods=['POST'])
# def login():
#     if User.login(request.form):
#         return redirect('/dashboard')
#     return redirect('/')

@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/')
