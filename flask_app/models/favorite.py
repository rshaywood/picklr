from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, favorite
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class Favorite:
    db = 'picklr'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.street_address = data['street_address']
        self.city = data['city']
        self.state = data['state']
        self.zip_code = data['zip_code']
        self.user_id = data['user_id']