import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

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


