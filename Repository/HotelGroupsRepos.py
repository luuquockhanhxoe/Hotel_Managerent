from Repository import QueryBase

def select_all_hotelgroups():
    select_Data = ("*",)
    return QueryBase.view_data_to_table(select_Data, "hotelgroup")

def select_one_hotelgroups(id):
    select_Data = ("*",)
    where = {"hotel_group_id": id}
    return QueryBase.view_data_to_table_conditions(select_Data,"hotelgroup", where)

def select_hotelgroup(data):
    select_Data = ("hotel_group_name",)
    where = {"hotel_group_name": data["hotel_group_name"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"hotelgroup", where)

def insert_hotel_group(data):
    columns = {"hotel_group_name": data["hotel_group_name"],
               "description": data["description"],
               "image": data["image"]}
    return QueryBase.add_data_to_table("hotelgroup", columns)

def update_hotel_group(id,data):
    update_column = {"hotel_group_name": data['hotel_group_name'],
                     "description": data["description"]}
    where = {"hotel_group_id": id}
    return QueryBase.update_data_to_table("hotelgroup",update_column, where)

def delete_hotel_group(id):
    where = {"hotel_group_id": id}
    return QueryBase.delete_data_to_table_conditions("hotelgroup", where)
