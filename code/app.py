from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "henrique"
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(
            filter(lambda x: x["name"] == name, items), None
        )  # First item matched by the filter function. If next doesn't find an item, it will return a None
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": f"An item with name '{name}' already exists."}, 400
        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}, 200


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
