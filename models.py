from config import db
from datetime import datetime


class Item_Model(db.Model):
    __tablename__ = 'items'

    post_id = db.Column(db.Integer, primary_key=True, autoincrement="auto")
    user_id = db.Column(db.String, nullable=False)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    condition = db.Column(db.String)


class User_Model(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String, primary_key=True)
    pref_name = db.Column(db.String, nullable=False)

# run first time only:
#db.create_all()
