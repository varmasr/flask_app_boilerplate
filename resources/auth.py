from flask_restful import Resource
from flask import request

from database.models import User

class SignupApi(Resource):
    
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id':str(id)}, 200