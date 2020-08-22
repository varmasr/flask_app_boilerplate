from .movie_restful import MovieApi, MoviesApi
from .auth import SignupApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi,'/api/movies/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
