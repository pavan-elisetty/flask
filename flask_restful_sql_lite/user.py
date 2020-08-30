import sqlite3
from flask_restful import Resource , reqparse
class User:
    def __init__(self , _id , username , password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls , username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query , (username,)) #for a single value tuple a comma is must
        row = result.fetchone() #fetches 1
        if row:
            #user = cls(row[0] , row[1] , row[2])
            #row[0] is id , row[1] is username
            user = cls(*row)
        else: #cls is User class
            user = None

        connection.close() #connection.commit isnt requred since we didnt add any data
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  # for a single value tuple a comma is must
        row = result.fetchone()  # fetches 1
        if row:
            #user = cls(row[0], row[1], row[2])
            # row[0] is id , row[1] is username
            user = cls(*row)
        else:  # cls is User class
            user = None

        connection.close()  # connection.commit isnt requred since we didnt add any data
        return user


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

        if User.find_by_username(data['username']):
            return {'message':'A user with that username already exists'}


        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL , ? , ?)" #here in Null it will auto increment
        cursor.execute(query , (data['username'] , data['password'],))

        connection.commit()
        connection.close()

        return {"message": "user created sucessfully"} , 201 #201 for created



