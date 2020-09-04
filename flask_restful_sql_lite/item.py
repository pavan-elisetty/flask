from flask_restful import Resource , reqparse
from flask_jwt import jwt_required
import sqlite3






class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,  # making price mandatory
                        help='This field cannot be left blank'
                        )

    #data = parser.parse_args()
    @jwt_required()
    def get(self , name):
        item = self.find_by_name(name)
        if item:
            return item

        return {'message':'item not found'} , 404

#while using flask restful we dont need to do jsonify as it already does that


    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': row[0], 'price': row[1]}

    def post(self , name):

        if self.find_by_name(name):
            return{'message':'An item with name {} already existed!'.format(name)} , 400

        data = Item.parser.parse_args()
        item = {'name':name , 'price':data['price']}

        try:
            self.insert(item)
        except:
            return {"message":"an error occured inserting an item"} , 500 #internal server error



        return item , 201 #201 code for creating

    @classmethod
    def insert(cls , item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return {'message':'item deleted'}


    def put(self , name):

        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] ==name , items) , None)
        #None return if nothing matches
        if item is None:
            item = {'name':name , 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item





class ItemList(Resource):
    def get(self):
        return {'items':items}
