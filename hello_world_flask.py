from flask import Flask

app = Flask(__name__)

@app.route('/') #http://google.com/' <-- forward slash mean homepage
def home():
    return 'Hello World!!'

app.run(port=4999)
