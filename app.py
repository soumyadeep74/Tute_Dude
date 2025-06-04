from flask import Flask, request, redirect, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.task2
collection = db['git_collection']

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    
    if item_name and item_desc:
        collection.insert_one({
            'name': item_name,
            'description': item_desc
        })
        return "Item added successfully!"
    return "Missing item name or description", 400

if __name__ == '__main__':
    app.run(debug=True)

