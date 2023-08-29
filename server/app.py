from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin


app = Flask(__name__)


app.config['MONGO_URI']=''
mongo = PyMongo(app)

@app.route("/")
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=true)