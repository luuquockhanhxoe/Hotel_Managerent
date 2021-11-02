from Repository import LoginRepos
from Handler import LoginAPI
from flask import json, jsonify
import jwt
import datetime

secret_key = "signature"

def login(data):
    check_username = LoginRepos.select_user_name(data)
    if check_username:
        check_password = LoginRepos.select_password(data)
        if check_password:
            check_user = LoginRepos.select_user_having(data)
            token = jwt.encode({"user_group_name": check_user["user_group_name"],
                                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                                secret_key)
            return jsonify({"jwt_token": token})
        else:
            return jsonify({"message": "Mật khẩu sai"})
    else:
        return jsonify({"message": "Không có tài khoản này"})