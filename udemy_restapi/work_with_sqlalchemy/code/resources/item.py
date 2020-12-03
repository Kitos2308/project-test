
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field can't be left blank!")

    #@app.route('/student/<string:name>')
    @jwt_required()
    def get(self, name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json() # now we add ItemModel and then ItemModel return ItemModel object but jwt required return json -> item.json()
        return {"message": "Item not found"}, 404





    def post(self, name):
        if ItemModel.find_by_name(name):
            return{"message": "An item with name '{}' already exists" .format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.insert()
        except:
            return {"message": "An error occured inserting item"}, 500

    def delete(self, name):
        if ItemModel.find_by_name(name):
            data=Item.parser.parse_args()
            item ={"name": name, 'price': data['price']}

            connection = sqlite3.connect('data.db')
            cursor=connection.cursor()
            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (name,))
            connection.commit()
            connection.close()
            return {'message': 'Item deleted'}, 201
        return {'message': "Item did not found"} ,400



    def put(self, name):
        if ItemModel.find_by_name(name):
            data = Item.parser.parse_args()
            item = ItemModel( name, data['price'])

            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query="UPDATE items SET price=? WHERE name=?"
            cursor.execute(query, (data['price'],name))
            connection.commit()
            connection.close()
            return {"message": "Item updated"}
        else:
            data = Item.parser.parse_args()
            item = ItemModel(name, data['price'])
            try:
                item.insert()
            except:
                return {"message": "An error occured inserting item"},500


            return item, 201






class Itemlist(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result=cursor.execute(query)
        items=[]
        for row in result:
            items.append({"name": row[0], "price": row[1]})

        connection.close()
        return {"items": items}