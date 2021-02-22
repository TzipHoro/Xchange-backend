from flask_restful import Resource, abort, marshal_with
from config import app, api, db
from args import resource_fields, item_put_args, item_update_args
from models import Item_Model


class Item(Resource):
    @marshal_with(resource_fields)
    def get(self, ID):
        result = Item_Model.query.filter_by(post_id=ID).first()
        if not result:
            abort(404, message="Post Id does not exist...")
        return result

    @marshal_with(resource_fields)
    def put(self, ID):
        args = item_put_args.parse_args()
        result = Item_Model.query.filter_by(post_id=ID).first()
        if result:
            abort(409, message="Post Id already exists...")
        item = Item_Model(post_id=ID, user_id=args['user_id'], title=args['title'], description=args['description'],
                          image=args['image'], date=args['date'], condition=args['condition'])
        db.session.add(item)
        db.session.commit()
        return item, 201

    @marshal_with(resource_fields)
    def patch(self, ID):
        args = item_update_args.parse_args()
        result = Item_Model.query.filter_by(post_id=ID).first()
        if not result:
            abort(404, message="Post Id does not exist...")

        if args['user_id']:
            result.user_id = args['user_id']
        if args['title']:
            result.title = args['title']
        if args['description']:
            result.description = args['description']
        if args['image']:
            result.image = args['image']
        if args['date']:
            result.date = args['date']
        if args['condition']:
            result.condition = args['condition']

        db.session.commit()

        return result

    @marshal_with(resource_fields)
    def delete(self, ID):
        # ...
        return '', 204


api.add_resource(Item, '/item/<int:ID>')

if __name__ == '__main__':
    app.run(debug=True)
