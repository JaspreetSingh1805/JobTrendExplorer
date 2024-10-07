from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['Job_listing']
collection = db['Job_data']

# API to fetch all data
@app.route('/data', methods=['GET'])
def fetch_all_data():
    data = list(collection.find({}, {'_id': False}))  # Exclude _id from the output
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
