from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate , identity
from resources.user import UserRegister
from resources.item import Item , ItemList



app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app , authenticate , identity) #creates new endpoint /auth


api.add_resource(ItemList , '/items')

api.add_resource(Item , '/item/<string:name>')
api.add_resource(UserRegister , '/register')

if __name__ == '__main__':

    app.run( port = 5000 , debug=True)
#this prevents from error and app.run will work only if it is run as primary
#but not called from other file