from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


# New Feature : User who created the movie only delete or edit the movie

class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(),required=True)
    genres = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')

   

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    #TODO : Need to understand in detail below code.
    # If a movie is deleted then movie should be pulled from the user document
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self,password):
        return check_password_hash(self.password, password)


# If a user is deleted then the movie created by the user is also deleted
User.register_delete_rule(Movie, 'added_by', db.CASCADE)