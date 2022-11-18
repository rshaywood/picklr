from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import request, session, flash
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
        self.user_favorites = []

# CREATE

    @classmethod
    def add_favorite(cls, data):
        query = """
        INSERT INTO locations (name, street_address, city, state, zip_code)
        VALUES (%(name)s, %(street_address)s, %(city)s, %(state)s, %(zip_code)s)
        ;"""
        location_id = connectToMySQL(cls.db).query_db(query, data)
        print('*****************', location_id) 
        return location_id

    @classmethod
    def get_all_favorites(cls):
        query = """SELECT * FROM locations;"""
        locations_from_db = connectToMySQL(cls.db).query_db(query)
        list_of_favorites_data = []
        for row in locations_from_db:
            list_of_favorites_data.append(cls(row))
        return list_of_favorites_data

    @classmethod
    def get_users_favorites(cls, data):
        query = """
        SELECT * 
        FROM locations
        LEFT JOIN favorites ON favorites.location_id=locations.id
        LEFT JOIN users ON favorites.user_id = users.id
        WHERE locations.id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if not results:
            return results
        favorite = cls(results[0])
        for favorite_from_db in results:
            favorite_data = {
                "name": favorite_from_db['name'],
                "street_address": favorite_from_db['street_address'],
                "city": favorite_from_db['city'],
                "state": favorite_from_db['state'],
                "zip_code": favorite_from_db['zip_code'],
            }
            favorite.user_favorites.append(user.User(favorite_data))
        return favorite

# VALIDATE - SQL

    # @staticmethod
    # def validate_location_info(favorite):
    #     is_valid = True
    #     query = "SELECT * FROM locations WHERE id = %(id)s;"
    #     results = connectToMySQL(Favorite.db).query_db(query, favorite)
    #     print(results)
    #     if not favorite['name']:
    #         flash("Facility name must be at least 3 characters.","create_favorite")
    #         is_valid= False
    #     if len(favorite['street_address']) < 3:
    #         flash("Facility address must be at least 3 characters.","create_favorite")
    #         is_valid= False
    #     if len(favorite['city']) < 1:
    #         flash("Please include the city.","create_favorite")
    #         is_valid= False
    #     if len(favorite['state']) < 1:
    #         flash("Please enter a state.","create_favorite")
    #         is_valid= False
    #     if len(favorite['zip_code']) < 5:
    #         flash("Please enter a valid zip code.","create_favorite")
    #         is_valid= False
    #     return is_valid

