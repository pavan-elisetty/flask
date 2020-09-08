from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate , identity
from resources.user import UserRegister
from resources.item import Item , ItemList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #this means that the sql-alchemy database livesinrootfolder
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app , authenticate , identity) #creates new endpoint /auth


api.add_resource(ItemList , '/items')

api.add_resource(Item , '/item/<string:name>')
api.add_resource(UserRegister , '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run( port = 5000 , debug=True)
#this prevents from error and app.run will work only if it is run as primary
#but not called from other file