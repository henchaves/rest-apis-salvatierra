from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "henrique"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True, help="This field cannot be left blank!")

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)  # First item matched by the filter function. If next doesn't find an item, it will return a None
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": f"An item with name '{name}' already exists."}, 400
        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201
    
    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item deleted."}
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
            return item, 201
        else:
            item.update(data)
            return item, 200


class ItemList(Resource):
    def get(self):
        return {"items": items}, 200


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
