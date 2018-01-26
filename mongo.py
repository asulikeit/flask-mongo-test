from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from tika import parser

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'srcdata'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/srcdata'

mongo = PyMongo(app)

@app.route('/pdf/<path:filename>', methods=['POST'])
def save_file(filename):
        filedb = mongo.db.files
        filename = '/' + filename
        parsed = parser.from_file(filename)
        doc = { 'filename' : filename,
                'contents' : parsed }
        filedb.save(doc)
        return "done: %s \n" % filename

@app.route('/pdf/<path:filename>', methods=['GET'])
def read_file(filename):
        filedb = mongo.db.files
        #text = filedb.find({"filename":"/home/daniel/flask/korean.rdf"}, {"_id":false,"contents.content":true})
        text = filedb.find_one({"filename":filename})
        print("test" + text)
        return jsonify({'result' : filename})

if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')
