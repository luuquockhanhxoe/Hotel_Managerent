from Repository import QueryBase

def select_all_users():
    select_Data = ("*",)
    return QueryBase.view_data_to_table(select_Data, "users")

def select_one_users(id):
    select_Data = ("*",)
    where = {"user_id": id}
    return QueryBase.view_data_to_table_conditions(select_Data,"users", where)

def select_user(data):
    select_Data = ("user_name",)
    where = {"user_name": data["user_name"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"users", where)

def insert_user(data):
    columns = {"user_name": data["user_name"],
               "password": data["password"],
               "user_group_id": data["user_group_id"]}
    return QueryBase.add_data_to_table("users", columns)

def update_user(id,data):
    update_column = {"user_name": data['user_name'],
                     "password": data["password"],
                     "user_group_id": data["user_group_id"]}
    where = {"user_id": id}
    return QueryBase.update_data_to_table("users",update_column, where)

def delete_user(id):
    where = {"user_id": id}
    return QueryBase.delete_data_to_table_conditions("users", where)