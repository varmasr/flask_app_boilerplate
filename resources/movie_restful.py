from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.models import Movie,User




class MoviesApi(Resource):

    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        movie = Movie(**body, added_by=user).save()
        # push__movies ??
        user.update(push__movies = movie)
        user.save()
        id = movie.id
        return {'id': str(id)}, 200

class MovieApi(Resource):
    
    @jwt_required
    def put(self, id):
        body = request.get_json()
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        movie.update(**body)
        return 'updated', 200
    
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        movie.delete()
        return "Deleted", 200
    
    def get(self, id):
        movie = Movie.objects.get(id=id).to_json()
        return Response(movie, mimetype="application/json", status=200)


    
