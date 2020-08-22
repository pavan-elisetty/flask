from flask import Flask,jsonify

app = Flask(__name__)

stores=[
    {
        'name':'My Wonderful store',
        'items':[     #by keeping the items in the list we can have many dictionaries ,i.e., many items
            {
                'name':'MY item',
                'price':15.99
            }
        ]
    }
]

#BROWSER PERSPECTIVE
#POST -- recieve data
#GET -- used to send data back

#POST /STORE data :{name}
@app.route('/store',methods=['POST'])
def create_store():
    pass
#GET /Store/<string:name>
@app.route('/store/<string:name>')  #'http://127.0.0.1.4999/store/some_name

def get_store(name):
    pass

#GET/store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}) # jsonify converts into json

#POST/store/<string:name/item
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store():
    pass
#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass

app.run(port=4998)