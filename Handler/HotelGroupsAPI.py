from flask import request
from flask import json
from Service import HotelGroupsService
from flask import Blueprint
hotelgroupsApi = Blueprint("hotelgroupsApi", __name__)

@hotelgroupsApi.route('/hotelgroups', methods = ['GET'])
def get_hotelgroups():
    #lấy tất cả thông tin cơ bản của hotelgroups.
    return HotelGroupsService.show_all_hotelgroups()

@hotelgroupsApi.route('/hotelgroups', methods = ['POST'])
def post_hotelgroup():
    #thêm thông tin cơ bản của hotelgroups.
    data = request.json
    return HotelGroupsService.add_hotelgroups_to_data(data)

@hotelgroupsApi.route('/hotelgroups/<id>', methods = ['PUT'])
def put_hotelgroup(id):
    #sửa hotelgroup
    data = request.json
    return HotelGroupsService.change_hotelgroups(id,data)


@hotelgroupsApi.route('/hotelgroups/<id>', methods = ['DELETE'])
def delete_hotelgroup(id):      
#xóa hotelgroups
    data = request.json
    return HotelGroupsService.delete_hotelgroups(id)


@hotelgroupsApi.route('/hotelgroups/<id>', methods = ['GET'])
def get_hotelgroup(id):  
#lấy thông tin cơ bản của hotelgroup theo id
    return HotelGroupsService.show_one_hotelgroups(id)
