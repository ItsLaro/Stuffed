from flask import Flask, jsonify, request
from flask.ext.pymongo import pymongo

db = Flask(__name__)

db.config['MONGO_DBNAME'] = "Stuffed_Rest"
db.config["MONGO_URI"] = "mongodb+srv://Laro:M4Wlkn1hE4nEmNHm@stuffed-6eadv.gcp.mongodb.net/test"
mongo = PyMongo(db)

@app.route('/item', methods=['GET'])
def get_all_items():
    item = mongo.db.item
     
    output = []

    for query in item.find():
        output.append({'name' : query['name'], 'quantity' : query['quantity'], 'storage' : query['storage']})

    return jsonify({'name' : output})

@app.route('/item', methods=['GET'])
def get_one_item(name):
    item = mongo.db.item

    query = item.find_one({'name' : name})
    output = {'name' : query['name'], 'quantity' : query['quantity'], 'storage' : query['storage']}

@app.route('/item', methods=['POST'])
def add_item():
    item = mongo.db.item

    name = request.json['name']
    quantity = request.json['quantity']
    storage = request.json['storage']

    item_id = item.insert({'name' : name, 'quantity' : quantity, 'storage' : storage})
    new_item = item.find_one({'_id' : item_id})

    output = {'name' : new_item['name'], 'quantity' : new_item['quantity'], 'storage' : new_item[storage]}

    return jsonify({'result' : output})

if __name__ == "__main__":
    app.run(debug=True)