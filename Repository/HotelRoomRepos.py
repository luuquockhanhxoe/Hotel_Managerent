from Repository import QueryBase

def select_all_hotelrooms():
    select_Data = ("*",)
    return QueryBase.view_data_to_table(select_Data, "hotelroom")

def select_one_hotelrooms(id):
    select_Data = ("*",)
    where = {"hotel_room_id": id}
    return QueryBase.view_data_to_table_conditions(select_Data,"hotelroom", where)

def select_hotelroom(data):
    select_Data = ("hotel_room_name",)
    where = {"hotel_room_name": data["hotel_room_name"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"hotelroom", where)

def insert_hotel_room(data):
    columns =  {'hotel_room_name': data['hotel_room_name'],
                'hotel_group_id': data['hotel_group_id'],
                'status': data['status'],
                'price': data['price'],
                'kind_of_room': data['kind_of_room'],
                'hotline_room': data['hotline_room']}
    return QueryBase.add_data_to_table("hotelroom", columns)

def update_hotel_room(id,data):
    update_column = {'hotel_room_name': data['hotel_room_name'],
                     'hotel_group_id': data['hotel_group_id'],
                     'status': data['status'],
                     'price': data['price'],
                     'kind_of_room': data['kind_of_room'],
                     'hotline_room': data['hotline_room']}
    where = {"hotel_room_id": id}
    return QueryBase.update_data_to_table("hotelroom",update_column, where)

def delete_hotel_room(id):
    where = {"hotel_room_id": id}
    return QueryBase.delete_data_to_table_conditions("hotelroom", where)
