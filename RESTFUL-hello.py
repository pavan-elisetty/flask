from flask import Flask
from flask_restful import Resource , Api

app = Flask(__name__)

api = Api(app)

class hello(Resource):
    def get(self , name):
        return {'hello':name}


api.add_resource(hello , '/hello/<string:name>')
#http://127.0.0.1:5000/student/name


app.run(port=5000)