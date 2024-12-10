from flask import Flask,request,jsonify
import json

app=Flask(__name__)


items=[
    {'id':1,'item':'item1','description':"This is item1"},
    {'id':2,'item':'item2','description':"This is item2"}
]


@app.route('/')
def home():
    return "<h1>Welcome To my Sample To do list App<h1>"


@app.route('/items',methods=['GET'])
def get_item():
    return jsonify(items)


@app.route('/items/<int:item_id>',methods=['GET'])
def get_item_id(item_id):
    item=next((item for item in items if item['id']==item_id),None)

    if item is None:
        return {'error':'Item not found'}
    return jsonify(item)


@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error":"item is not found"})

    new_item={
        "id":items[-1]['id']+1 if item else 1 ,
        "name":request.json['name'],
        "description":request.json['description']
    }


    items.append(new_item)

    return jsonify(new_item)



@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if items['id']==item_id))
    if not item:
        return {'error':'item not found'}

    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])

    return jsonify(item)


@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]

    return jsonify({'error':'item deleted'})

    

if __name__=='__main__':
    app.run(debug=True)