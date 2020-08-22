from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from database.models import Movie




class MoviesApi(Resource):

    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200

class MovieApi(Resource):
    
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return 'updated', 200
    
    @jwt_required
    def delete(self, id):
        Movie.objects.get(id=id).delete()
        return "Deleted", 200
    
    def get(self, id):
        movie = Movie.objects.get(id=id).to_json()
        return Response(movie, mimetype="application/json", status=200)


    
