from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session, render_template, redirect, request
from flask_app.models import user
from flask_app.models import favorite
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/dashboard')
def view_dashboard():
    all_favorites = favorite.Favorite.get_all_favorites()
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', all_favorites = all_favorites, this_user=this_user)

@app.route('/location/add_form')
def view_add_form():
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('add_location.html', this_user=this_user)

@app.route('/location/create', methods=['POST'])
def add_location():
    if 'user_id' not in session:
        return redirect('/')
    # if not favorite.Favorite.validate_location_info(request.form):
    #     return redirect('/location/add_form')
    data = {
        "name": request.form['name'],
        "street_address": request.form['street_address'],
        "city": request.form['city'],
        "state": request.form['state'],
        # "zip_code": request.form['zip_code']
    }
    favorite.Favorite.add_favorite(data)
    return redirect('/dashboard')