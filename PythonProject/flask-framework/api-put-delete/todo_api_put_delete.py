# Flask API PUT and DELETE HTTP Verbs
# Working with API's - Json

from flask import Flask, jsonify, request


app=Flask(__name__)

## Initialize Data into my todo list 
items = [
    {'id': 1, "name": "Item 1", "Description": "This is item 1"},
    {'id': 2, "name": "Item 2", "Description": "This is item 2"}
    ]


@app.route('/')
def home():
    return "Welcome to the Sample ToDo list App"

## Get: Retrive all the items 
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Get: Retrive a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not foud"})
    return jsonify(item)

# Post: Create a new item 
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Item not foud"})
    
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        'description': request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')