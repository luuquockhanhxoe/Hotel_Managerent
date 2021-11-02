from Repository import QueryBase

def select_all_usergroups():
    select_Data = ("user_group_id","user_group_name")
    return QueryBase.view_data_to_table(select_Data, "usergroups")

def select_one_usergroups(id):
    select_Data = ("user_group_name",)
    where = {"user_group_id": id}
    return QueryBase.view_data_to_table_conditions(select_Data,"usergroups", where)

def select_usergroup(data):
    select_Data = ("user_group_name",)
    where = {"user_group_name": data["user_group_name"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"usergroups", where)

def insert_user_group(data):
    columns = {"user_group_name": data["user_group_name"]}
    return QueryBase.add_data_to_table("usergroups", columns)

def update_user_group(id,data):
    update_column = {"user_group_name": data['user_group_name'],}
    where = {"user_group_id":id}
    return QueryBase.update_data_to_table("usergroups",update_column, where)

def delete_user_group(id):
    where = {"user_group_id":id}
    return QueryBase.delete_data_to_table_conditions("usergroups", where)
