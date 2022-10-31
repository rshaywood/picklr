from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session, render_template
from flask_app.models import user
from flask_app.models import favorite
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/dashboard')
def view_dashboard():
    all_favorites = favorite.Favorite.get_all_favorites()
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', all_favorites = all_favorites, this_user=this_user)