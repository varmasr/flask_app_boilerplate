from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from resources.movie import movies
from resources.routes import initialize_routes



app = Flask(__name__)
api = Api(app)

# movies =  [
#     {
#         "name": "The Shawshank Redemption",
#         "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
#         "genres": ["Drama"]
#     },
#     {
#        "name": "The Godfather ",
#        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
#        "genres": ["Crime", "Drama"]
#     }
# ]

app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/movie-bag'
}

app.config.from_envvar('ENV_FILE_LOCATION')


initialize_db(app)

#app.register_blueprint(movies)
initialize_routes(api)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.run(debug=True)