from flask import Blueprint, request, Response
from database.models import Movie

movies = Blueprint('movies', __name__)

@movies.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@movies.route('/movies', methods=['POST'])
def add_movie():
   body = request.get_json()
   movie = Movie(**body).save()
   id = movie.id
   return {'id': str(id)}, 200

@movies.route('/movies/<id>', methods=(['PUT']))
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return 'updated', 200

@movies.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return "Deleted", 200