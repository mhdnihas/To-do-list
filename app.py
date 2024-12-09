from flask import Flask,request,jsonify
import json

app=Flask(__name__)


items=[
    {'id':1,'item':'item1','description':"This is item1"},
    {'id':2,'item':'item2','description':"This is item2"}
]


@app.route('/')
def home():
    return "Welcome To my Sample To do list App"


@app.route('/items',method=['GET'])
def get_item():
    return jsonify(items)


@app.route('items/<int:item_id>',method=['GET'])
def get_item_id(item_id):
    item=next((item for item in items if item['id']==item_id),None)

    if item is None:
        return {'error':'Item not found'}
    return jsonify(item)


@app.route('/items',method='POST')
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item is not found"})

    new_item={
        "id":items[-1]['item_id']+1 if item else 1 ,
        "name":request.json['name']
        "description":request.json['description']
    }


    items.append(new_item)

    return jsonify(new_item)

    

if __name__=='__main__':
    app.run(debug=True)