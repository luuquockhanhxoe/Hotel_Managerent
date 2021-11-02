from flask import jsonify
from flask import request
from werkzeug.wrappers.request import PlainRequest
from Service.Authentication import secret_key
import jwt
from jwt.exceptions import ExpiredSignatureError
from functools import wraps

class token():
    def token_register_user(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            jwt_token = None
            if "token" in request.headers:
                jwt_token = request.headers["token"]
            if not jwt_token:
                return jsonify({"message": "Token is missing!"}), 403
            try:
                payload = jwt.decode(jwt_token,key=secret_key,algorithms=["HS256", ])
                if payload["user_group_name"] != "registed User":
                    return jsonify({"message": "Can not perform that function"})
            except:
                return jsonify({"message": "Token is invalid"}), 403
            return f(payload,*args, **kwargs)
        return decorated

    def token_admin(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            jwt_token = None
            if "token" in request.headers:
                jwt_token = request.headers["token"]
            if not jwt_token:
                return jsonify({"message": "Token is missing!"}), 403
            try:
                payload = jwt.decode(jwt_token,key=secret_key,algorithms=["HS256", ])
                if payload["user_group_name"] != "admin":
                    return jsonify({"message": "Can not perform that function"})
            except:
                return jsonify({"message": "Token is invalid"}), 403
            return f(payload,*args, **kwargs)
        return decorated

    def token_manager(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            jwt_token = None
            if "token" in request.headers:
                jwt_token = request.headers["token"]
            if not jwt_token:
                return jsonify({"message": "Token is missing!"}), 403
            try:
                payload = jwt.decode(jwt_token,key=secret_key,algorithms=["HS256", ])
                if payload["user_group_name"] != "manager":
                    return jsonify({"message": "Can not perform that function"})
            except:
                return jsonify({"message": "Token is invalid"}), 403
            return f(payload,*args, **kwargs)
        return decorated


    def token_staff(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            jwt_token = None
            if "token" in request.headers:
                jwt_token = request.headers["token"]
            if not jwt_token:
                return jsonify({"message": "Token is missing!"}), 403
            try:
                payload = jwt.decode(jwt_token,key=secret_key,algorithms=["HS256", ])
                if payload["user_group_name"] != "staff":
                    return jsonify({"message": "Can not perform that function"})
            except:
                return jsonify({"message": "Token is invalid"}), 403
            return f(payload,*args, **kwargs)
        return decorated