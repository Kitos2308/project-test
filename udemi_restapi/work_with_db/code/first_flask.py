from flask import Flask, request

from flask_restful import Resource, Api, reqparse

from flask_jwt import JWT, jwt_required

from security import authenticate, identity

from user import UserRegister

app = Flask(__name__)
app.secret_key='jose'
api = Api(app)



jwt =JWT(app, authenticate, identity)

items = []



class Item(Resource):
    #@app.route('/student/<string:name>')
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name']==name, items), None)
        return {"item": item}, 200 if item  else 404


    def post(self, name):
        if next((filter(lambda x: x['name'] == name, items)), None) is not None:
            return{"message": "An item with name '{}' already exists" .format(name)}, 400

        data=request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items= list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price',
            type=float,
            required=True,
            help="This field can't be left blank!")

        data = parser.parse_args()

        print(data)
        item = next(filter(lambda x: x['name']==name, items), None)
        if item is None:
            item ={'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item



class Itemlist(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5001)






