from flask import Flask , request
from flask_restful import Resource , Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self , name):
        #next returns the first value returned by filter function
        item = next(filter( lambda x: x['name'] == name , items))
        return {'item':None} , 200 if item else 404


#while using flask restful we dont need to do jsonify as it already does that



    def post(self , name):
        if next(filter(lambda x: x['name'] == name, items)) is not None:
            return{'message':'An item with name {} already existed!'.format(name)} , 400


        data = request.get_json() # json pay load , if the data is not in the format of proper json then this will give an error
        #force = True   **better not use them
        #silent = True
        item = {'name':name , 'price':data['price']}
        items.append(item)
        return item , 201 #201 code for creating

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(ItemList , '/items')

api.add_resource(Item , '/item/<string:name>')

app.run( port = 5000 , debug=True)
