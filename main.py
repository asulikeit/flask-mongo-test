#-*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from tika import parser

import json
import platform
import splitter

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'srcdata'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/srcdata'

mongo = PyMongo(app)


@app.route('/pdf/<path:filepath>', methods=['POST'])
def save_file(filepath):
        filedb = mongo.db.files
        filename = get_filename(filepath)
        parsed = parser.from_file(filename)
        doc = { 'filename' : filename,
                'contents' : parsed }
        filedb.save(doc)
        return "done: %s \n" % filename


# Supported by TANDEM6
@app.route('/pdf/<path:filepath>', methods=['GET'])
def read_file(filepath):
        filedb = mongo.db.files
        filename = get_filename(filepath)
        textcnt = filedb.find({"filename":filename},
            {"_id":0, "contents.content":1})
        return dumps(textcnt)


@app.route('/doc/<path:filepath>', methods=['POST'])
def parse_doc(filepath):
        filename = get_filename(filepath)
        parsed = parser.from_file(filename)
        content = parsed['content']
        splited_content = splitter.split_tika_content(content)
        body = splited_content[1]
        return json.dumps(body, ensure_ascii=False).encode('utf-8')


def get_filename(filepath):
        if platform.system() == 'Windows':
            return filepath
        else:
            return '/' + filepath           


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
