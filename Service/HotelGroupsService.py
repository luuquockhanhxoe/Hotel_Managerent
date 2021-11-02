from Model.Setting import HotelGroup
from Repository import HotelGroupsRepos
from flask import jsonify


def show_all_hotelgroups():
    hotelgroups = HotelGroupsRepos.select_all_hotelgroups()
    try:
        output = []
        for hotelgroup in hotelgroups:
            hotelgroup = {'hotel_group_id': hotelgroup['hotel_group_id'],
                          'hotel_group_name': hotelgroup['hotel_group_name'],
                          'description': hotelgroup['description'],
                          'image': hotelgroup['image']}
            output.append(hotelgroup)
        return jsonify({"hotelgroups": output})
    except:
        return jsonify({"message": "Không có hotelgroup nào cả!"})


def add_hotelgroups_to_data(data):
    check_data = HotelGroupsRepos.select_hotelgroup(data)
    if check_data:
        return jsonify({"message": "Đã tồn tại hotel group name này!", 
                        "hotel_group": check_data})
    else: 
        HotelGroupsRepos.insert_hotel_group(data)
        hotel_group = HotelGroupsRepos.select_hotelgroup(data)
        return jsonify({"message": "Thêm thành công",
                        "hotelgroup": hotel_group})


def change_hotelgroups(id,data):
    check_data = HotelGroupsRepos.select_hotelgroup(data)
    if check_data:
        HotelGroupsRepos.update_hotel_group(id,data)
        hotel_group = HotelGroupsRepos.select_hotelgroup(data)
        return jsonify({"message": "Đổi dũ liệu hotel group thành công",
                        "hotelgroup": hotel_group})
    else :
        return jsonify({"message": "Đã tồn tại hotel group name này!",
                        "hotel_group": check_data})

def delete_hotelgroups(id):
    HotelGroupsRepos.delete_hotel_group(id)
    return jsonify({"message": "Xóa hotel group thành công"})

def show_one_hotelgroups(id):
    hotelgroup = HotelGroupsRepos.select_one_hotelgroups(id)
    try:
        hotel_data = {'hotel_group_id': hotelgroup['hotel_group_id'],
                      'hotel_group_name': hotelgroup['hotel_group_name'],
                      'description': hotelgroup['description'],
                      'image': hotelgroup['image']}
        return jsonify({"hotelgroup": hotel_data})
    except:
        return jsonify({"message": "Không có hotel group id này!"})
