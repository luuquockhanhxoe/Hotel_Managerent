from flask import request
from flask import json
from Service import HotelRoomService
from Handler.Middleware.Authorization import token
from flask import Blueprint
hotelroomsAPI = Blueprint("hotelroomsAPI", __name__)


@hotelroomsAPI.route('/hotelrooms', methods = ['GET'])
@token.token_staff
def get_hotelrooms(payload):
    #lấy tất cả thông tin cơ bản của hotelrooms.
    return HotelRoomService.show_all_hotelrooms()

@hotelroomsAPI.route('/hotelrooms', methods = ['POST'])
@token.token_staff
def post_hotelroom():
    #thêm thông tin cơ bản của hotelrooms.
    data = request.json
    return HotelRoomService.add_hotelrooms_to_data(data)

@hotelroomsAPI.route('/hotelrooms/<id>', methods = ['PUT'])
@token.token_staff
def put_hotelroom(id):
    #sửa hotelroom
    data = request.json
    return HotelRoomService.change_hotelrooms(id,data)


@hotelroomsAPI.route('/hotelrooms/<id>', methods = ['DELETE'])
@token.token_staff
def delete_hotelroom(id):      
#xóa hotelrooms
    data = request.json
    return HotelRoomService.delete_hotelrooms(id)


@hotelroomsAPI.route('/hotelrooms/<id>', methods = ['GET'])
@token.token_staff
def get_hotelroom(id):  
#lấy thông tin cơ bản của hotelroom theo id
    return HotelRoomService.show_one_hotelrooms(id)
