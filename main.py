from flask_restful import Resource, abort, marshal_with
from config import app, api, db
from args import resource_fields_item, item_put_args, item_update_args, user_put_args, user_update_args, \
    resource_fields_user
from models import Item_Model, User_Model


class Item(Resource):
    @marshal_with(resource_fields_item)
    def get(self, ID):
        result = Item_Model.query.filter_by(post_id=ID).first()
        if not result:
            abort(404, message="Post Id does not exist...")
        return result

    @marshal_with(resource_fields_item)
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

    @marshal_with(resource_fields_item)
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

    @marshal_with(resource_fields_item)
    def delete(self, ID):
        tmp = Item_Model.query.get(ID)

        db.session.delete(tmp)
        db.session.commit()

        abort(404, message='Item deleted')
        return -1


class User(Resource):
    @marshal_with(resource_fields_user)
    def get(self, ID):
        result = User_Model.query.filter_by(user_id=ID).first()
        if not result:
            abort(404, message="User Id does not exist...")
        return result

    @marshal_with(resource_fields_user)
    def put(self, ID):
        args = user_put_args.parse_args()
        result = User_Model.query.filter_by(user_id=ID).first()
        if result:
            abort(409, message="User Id already exists...")
        user = User_Model(user_id=ID, pref_name=args['pref_name'])
        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(resource_fields_user)
    def patch(self, ID):
        args = user_update_args.parse_args()
        result = User_Model.query.filter_by(user_id=ID).first()
        if not result:
            abort(404, message="User Id does not exist...")

        if args['pref_name']:
            result.pref_name = args['pref_name']

        db.session.commit()

        return result

    @marshal_with(resource_fields_user)
    def delete(self, ID):
        tmp = User_Model.query.get(ID)

        db.session.delete(tmp)
        db.session.commit()

        abort(404, message='User deleted')
        return -1


api.add_resource(Item, '/item/<int:ID>')
api.add_resource(User, '/user/<string:ID>')

if __name__ == '__main__':
    app.run(debug=True)
