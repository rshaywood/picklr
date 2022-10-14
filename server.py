from flask import Flask
from flask_app import app
from flask_app.controllers import users, favorites
from flask_app.models.favorite import Favorite
from flask_app.models.user import User

if __name__ == "__main__":
    app.run(debug=True)