from flask import request
from flask import json
from Service import ServicesService
from Handler.Middleware.Authorization import token
from flask import Blueprint
servicesApi = Blueprint("servicesApi", __name__)

@servicesApi.route('/services', methods = ['GET'])
@token.token_admin
def get_services(payload):
    #lấy tất cả thông tin cơ bản của services.
    return ServicesService.show_all_services()

@servicesApi.route('/services/create', methods = ['POST'])
@token.token_admin
def post_service():
    #thêm thông tin cơ bản của services.
    data = request.json
    return ServicesService.add_services_to_data(data)

@servicesApi.route('/services/<id>', methods = ['PUT'])
@token.token_admin
def put_service(id):
    #sửa hservices
    data = request.json
    return ServicesService.change_services(id,data)


@servicesApi.route('/services/<id>', methods = ['DELETE'])
@token.token_admin
def delete_service(id):      
    #xóa services
    data = request.json
    return ServicesService.delete_services(id)


@servicesApi.route('/services/<id>', methods = ['GET'])
@token.token_admin
def get_service(id):
    #lấy thông tin cơ bản của services theo id
    return ServicesService.show_one_services(id)
