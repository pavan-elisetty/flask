from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister,User,UserLogin
from resources.item import Item , ItemList
from resources.store import Store , StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #this means that the sql-alchemy database livesinrootfolder
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True  #if JWT raises error then flask doesnt care if its true
app.secret_key = 'jose' #app.config['JWT_SECRET_KEY']
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app) #not creating /auth end point
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity==1:   #Insted of hard-coding , you should read from a config file or a db
        return {'is_admin':True}
    return {'is_admin':False}





api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

api.add_resource(Item , '/item/<string:name>')
api.add_resource(ItemList , '/items')

api.add_resource(UserRegister , '/register')
api.add_resource(User,'/user/<int:user_id>')
api.add_resource(UserLogin,'/login')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run( port = 5000 , debug=True)
#this prevents from error and app.run will work only if it is run as primary
#but not called from other file