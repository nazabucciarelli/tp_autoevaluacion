from marshmallow import fields
from app import ma

class UserBasicSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    password = fields.String()

class PostSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    content = fields.String()
    user_id = fields.Integer()

class CommentarySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    content = fields.String()
    user_id = fields.Integer()
    post_id = fields.Integer()

class CategorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()




