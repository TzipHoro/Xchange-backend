from flask_restful import reqparse, fields
from datetime import datetime


# mandatory arguments
item_put_args = reqparse.RequestParser()

item_put_args.add_argument("user_id", type=str, help="User Id is required", required=True)
item_put_args.add_argument("title", type=str, help="Item title")
item_put_args.add_argument("description", type=str, help="Item description")
item_put_args.add_argument("image", type=str, help="Post image")
item_put_args.add_argument("date", type=datetime, help="Timestamp")
item_put_args.add_argument("condition", type=str, help="Item condition")

# update arguments
item_update_args = reqparse.RequestParser()

item_update_args.add_argument("user_id", type=str, help="User Id is required")
item_update_args.add_argument("title", type=str, help="Item title")
item_update_args.add_argument("description", type=str, help="Item description")
item_update_args.add_argument("image", type=str, help="Post image")
item_update_args.add_argument("date", type=datetime, help="Timestamp")
item_update_args.add_argument("condition", type=str, help="Item condition")

resource_fields = {
    'post_id': fields.Integer,
    'user_id': fields.String,
    'title': fields.String,
    'description': fields.String,
    'image': fields.String,
    'date': fields.DateTime,
    'condition': fields.String
}