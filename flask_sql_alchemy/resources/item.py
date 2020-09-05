from flask_restful import Resource , reqparse
from flask_jwt import jwt_required
import sqlite3
#RESOURCES ARE SUMTNG WHERE ONLY THE CLIENTS INTERACT WITH LIKE API ENDPOINTS
from models.item import ItemModel




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
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message':'item not found'} , 404

#while using flask restful we dont need to do jsonify as it already does that



    def post(self , name):

        if ItemModel.find_by_name(name):
            return{'message':'An item with name {} already existed!'.format(name)} , 400

        data = Item.parser.parse_args()
        item = ItemModel(name,data['price']) #returning ItemModel object

        try:
            item.insert()
        except:
            return {"message":"an error occured inserting an item"} , 500 #internal server error



        return item.json() , 201 #201 code for creating


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
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name,data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {'message':'an error occured in inserting item'} , 500
        else:
            try:
                updated_item.update()
            except:
                return {'message':'an error occured updating the item'},500
        return updated_item.json()




class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result=cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})
        connection.close()

        return {'items':items}
