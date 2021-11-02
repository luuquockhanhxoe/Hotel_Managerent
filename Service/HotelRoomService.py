from Repository import HotelRoomRepos
from flask import jsonify


def show_all_hotelrooms():
    hotelrooms = HotelRoomRepos.select_all_hotelrooms()
    try:
        output = []
        for hotelroom in hotelrooms:
            hotelroom = {'hotel_room_id': hotelroom['hotel_room_id'],
                          'hotel_room_name': hotelroom['hotel_room_name'],
                          'hotel_group_id': hotelroom['hotel_group_id'],
                          'status': hotelroom['status'],
                          'price': hotelroom['price'],
                          'kind_of_room': hotelroom['kind_of_room'],
                          'hotline_room': hotelroom['hotline_room']}
            output.append(hotelroom)
        return jsonify({"hotelrooms": output})
    except:
        return jsonify({"message": "Không có hotelroom nào cả!"})


def add_hotelrooms_to_data(data):
    check_data = HotelRoomRepos.select_hotelroom(data)
    if check_data:
        return jsonify({"message": "Đã tồn tại hotel room name này!", 
                        "hotel_room": check_data})
    else: 
        HotelRoomRepos.insert_hotel_room(data)
        hotel_room = HotelRoomRepos.select_hotelroom(data)
        return jsonify({"message": "Thêm thành công",
                        "hotelroom": hotel_room})


def change_hotelrooms(id,data):
    check_data = HotelRoomRepos.select_hotelroom(data)
    if check_data:
        return jsonify({"message": "Đã tồn tại hotel room name này!",
                        "hotel_room": check_data})
    else :    
        HotelRoomRepos.update_hotel_room(id,data)
        hotel_room = HotelRoomRepos.select_hotelroom(data)
        return jsonify({"message": "Đổi dũ liệu hotel room thành công",
                        "hotelroom": hotel_room})

def delete_hotelrooms(id):
    HotelRoomRepos.delete_hotel_room(id)
    return jsonify({"message": "Xóa hotel room thành công"})

def show_one_hotelrooms(id):
    hotelroom = HotelRoomRepos.select_one_hotelrooms(id)
    try:
        hotel_data = {'hotel_room_id': hotelroom['hotel_room_id'],
                      'hotel_room_name': hotelroom['hotel_room_name'],
                      'hotel_group_id': hotelroom['hotel_group_id'],
                      'status': hotelroom['status'],
                      'price': hotelroom['price'],
                      'kind_of_room': hotelroom['kind_of_room'],
                      'hotline_room': hotelroom['hotline_room']}
        return jsonify({"hotelroom": hotel_data})
    except:
        return jsonify({"message": "Không có hotel room id này!"})
