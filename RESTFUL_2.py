from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self , name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item':None} , 404 #404 for error code


#while using flask restful we dont need to do jsonify as it already does that

    def post(self , name):
        item = {'name':name , 'price':12.00}
        items.append(item)
        return item , 201 #201 code for creating

api.add_resource(Item , '/item/<string:name>')

app.run()