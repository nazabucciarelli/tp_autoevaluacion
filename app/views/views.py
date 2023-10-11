from app import app, db

from flask import (
    jsonify,
    request
)
from app.models.models import User
from app.schemas.schemas import UserBasicSchema

from flask.views import MethodView

class UserAPI(MethodView):
    def get(self,user_id=None):
        if user_id is None:
            users = User.query.all()
            users_schema = UserBasicSchema().dump(users,many=True) # Dump convierte el objeto a schema
            return jsonify(users_schema)
        user = User.query.get(user_id)
        user_schema = UserBasicSchema().dump(user)
        return jsonify(user_schema)
        
    def post(self):
        user_json = UserBasicSchema().load(request.json) # Load convierte el json a schema
        username = user_json.get('username')
        password = user_json.get('password')
        new_user= User(username=username,password=password,visible=1)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(msg="post method")
    
    def put(self, user_id):
        user = User.query.get(user_id)
        user_json= UserBasicSchema().load(request.json)
        username = user_json.get("username")
        password = user_json.get("password")
        user.username = username
        user.password = password
        db.session.commit()
        return jsonify(UserBasicSchema().dump(user))
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        user.visible = 0
        db.session.commit()
        return jsonify(msg="user deleted")
    
app.add_url_rule("/user",view_func=UserAPI.as_view('user'))
app.add_url_rule("/user/<user_id>",
                 view_func=UserAPI.as_view('user_id'))
