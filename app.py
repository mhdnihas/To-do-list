from flask import Flask, request, jsonify, render_template,url_for

app = Flask(__name__)

items = [
    {'id': 1, 'item': 'item1', 'description': "This is item1"},
    {'id': 2, 'item': 'item2', 'description': "This is item2"}
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return {'error': 'Item not found'}
    return jsonify(item)


@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Item name is required"})

    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "item": request.json['name'],
        "description": request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item)


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)

    if not item:
        return {'error': 'Item not found'}

    item['item'] = request.json.get('name', item['item'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]

    return jsonify({'message': 'Item deleted'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
