import sqlite3
from flask_restful import Resource , reqparse
from models.user import UserModel

class UserRegister(Resource):
    #getting data from json payload
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="this field cannot be blank."
                        )
    #parser for getting inputs

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':'A user with that username already exists'}


        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL , ? , ?)" #here in Null it will auto increment
        cursor.execute(query , (data['username'] , data['password'],))

        connection.commit()
        connection.close()

        return {"message": "user created sucessfully"} , 201 #201 for created



