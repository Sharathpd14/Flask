from flask import Flask, jsonify,request


app = Flask(__name__)

items =[
    {"id":10, "Name":"Walk","Description":"Walk 2000m"},
    {"id":20,"Name":"Eat","Description":"Have breakfast"}
]

@app.route('/')
def home():
    return "Welcome to this new flask course"


# Retrieve all the items
@app.route('/items',methods=["GET"])
def get_items():
    return jsonify(items)

# GET : Retrive specific item based on id
@app.route("/items/<int:item_id>",methods = ["GET"])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    else:
        return jsonify(item)
    
    
# POST : Create a new task
@app.route("/items",methods = ["POST"])
def create_item():
    if not request.json or "Name" not in request.json:
        return jsonify({"error":"Item not fount"})
    else:
        new_item = {
            "id" : items[-1]["id"]+1 if items else 1,
            "Name":request.json["Name"],
            "Description":request.json["Description"]
        }
        items.append(new_item)
    return jsonify(new_item)
    
    
# PUT : Update an existing item
@app.route("/items/<int:item_id>",methods = ["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item["Name"] = request.json.get('Name',item['Name'])
    item["Description"] = request.json.get('Description',item['Description'])
    return jsonify(item)


# DELETE : Delete an item
@app.route("/items/<int:item_id>",methods = ["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"Result":"Item deleted"})
    

if __name__ == "__main__":
    app.run(debug=True)