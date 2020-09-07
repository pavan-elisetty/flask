import sqlite3

#models are sumtng which works internally , used for internal representation
from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer , primary_key = True)
    name=db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))



    def __init__(self,name,price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name , 'price':self.price}

    @classmethod
    def find_by_name(cls, name): #cls==ItemModel
        return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1


    def save_to_db(self):
        db.session.add(self)   #this method is useful to both update and insert
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()