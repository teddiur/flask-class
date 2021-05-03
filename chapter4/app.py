from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return {'status': 'success', 'item': {**item}}
        return {'status': 'failed'}, 404

    def post(self, name):
        item = {'name': name, 'price': 12}
        items.append(item)
        return {'status': 'success', 'item': {**item}}, 201


class Items(Resource):
    def get(self):
        return items


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
