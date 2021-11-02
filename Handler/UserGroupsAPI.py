from Model.Setting import Services
from Service import UserGroupsService
from flask import request
from flask import jsonify
from flask import Blueprint
userroupsApi = Blueprint("userroupsApi", __name__)


@userroupsApi.route('/usergroups', methods = ['GET'])
def get_usergroups():
    #lấy tất cả thông tin cơ bản của usergroups.
    return UserGroupsService.show_all_usergroups()

@userroupsApi.route('/usergroups', methods = ['POST'])
def post_usergroup():
    #thêm thông tin cơ bản của usergroups.
    data = request.json
    return UserGroupsService.add_usergroups_to_data(data)

@userroupsApi.route('/usergroups/<id>', methods = ['PUT'])
def put_usergroup(id):
    #sửa usergroup
    data = request.json
    return UserGroupsService.change_usergroups(id,data)


@userroupsApi.route('/usergroups/<id>', methods = ['DELETE'])
def delete_usergroup(id):      
#xóa usergroups
    data = request.json
    return UserGroupsService.delete_usergroups(id)


@userroupsApi.route('/usergroups/<id>', methods = ['GET'])
def get_usergroup(id):  
#lấy thông tin cơ bản của usergroup theo id
    return UserGroupsService.show_one_usergroups(id)
