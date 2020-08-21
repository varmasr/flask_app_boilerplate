from flask import Flask
from database.db import initialize_db
from resources.movie import movies


app = Flask(__name__)

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

initialize_db(app)

app.register_blueprint(movies)


app.run(debug=True)