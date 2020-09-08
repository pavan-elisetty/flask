from flask_restful import Resource , reqparse
from flask_jwt import jwt_required
#RESOURCES ARE SUMTNG WHERE ONLY THE CLIENTS INTERACT WITH LIKE API ENDPOINTS
from models.item import ItemModel




class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,  # making price mandatory
                        help='This field cannot be left blank'
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,  # making price mandatory
                        help='Every item needs a store id'
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
        item = ItemModel(name, **data) #returning ItemModel object
        #data['price'],data['store_id']
        try:
            item.save_to_db()
        except:
            return {"message":"an error occured inserting an item"} , 500 #internal server error



        return item.json() , 201 #201 code for creating


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'item deleted'}


    def put(self , name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name , data['price'],data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()




class ItemList(Resource):
    def get(self):
        return {'items':[x.json() for x in ItemModel.query.all()]}
        #return{'items':list(map(lambda x:x.json(),ItemModel.query.all()))}