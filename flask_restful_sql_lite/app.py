from flask import Flask , request
from flask_restful import Resource , Api , reqparse
from flask_jwt import JWT , jwt_required
from security import authenticate , identity
from user import UserRegister

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)
jwt = JWT(app , authenticate , identity) #creates new endpoint /auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,  # making price mandatory
                        help='This field cannot be left blank'
                        )

    data = parser.parse_args()
    @jwt_required()
    def get(self , name):
        #next returns the first value returned by filter function
        item = next(filter( lambda x: x['name'] == name , items))
        return {'item':None} , 200 if item else 404


#while using flask restful we dont need to do jsonify as it already does that



    def post(self , name):


        if next(filter(lambda x: x['name'] == name, items) , None) is not None:
            return{'message':'An item with name {} already existed!'.format(name)} , 400

        data = Item.parser.parse_args()
        item = {'name':name , 'price':data['price']}
        items.append(item)
        return item , 201 #201 code for creating

    def delete(self, name):
        global items
        items = list(filter(lambda x:x['name']!=name,items))
        return {'message':'item deleted'}
        #filtering the items adding all the items except the item that needs to be deleted


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

api.add_resource(ItemList , '/items')

api.add_resource(Item , '/item/<string:name>')
api.add_resource(UserRegister , '/register')

#app.run( port = 5000 , debug=True)
if __name__ == '__main__':
    app.run(debug=True)
