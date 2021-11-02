from Model.Setting import Services
from Service import UsersService
from flask import request
from flask import json
from flask import Blueprint
usersApi = Blueprint("usersApi", __name__)


@usersApi.route('/users', methods = ['GET'])
def get_users():
    #lấy tất cả thông tin cơ bản của users.
    return UsersService.show_all_users()

@usersApi.route('/users', methods = ['POST'])
def post_user():
    #thêm thông tin cơ bản của users.
    data = request.json
    return UsersService.add_users_to_data(data)

@usersApi.route('/users/<id>', methods = ['PUT'])
def put_user(id):
    #sửa users
    data = request.json
    return UsersService.change_users(id,data)


@usersApi.route('/users/<id>', methods = ['DELETE'])
def delete_user(id):      
#xóa user
    data = request.json
    return UsersService.delete_users(id)


@usersApi.route('/users/<id>', methods = ['GET'])
def get_user(id):  
#lấy thông tin cơ bản của users theo id
    return UsersService.show_one_users(id)
