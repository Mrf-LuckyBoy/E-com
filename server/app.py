from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin


app = Flask(__name__)


app.config['MONGO_URI']='mongodb+srv://Atsawa:091109@cluster0.uqtmipl.mongodb.net/?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route("/")
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=true)