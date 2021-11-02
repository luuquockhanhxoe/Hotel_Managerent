from Repository import QueryBase

def select_user_having(data):
    select_data = ("users.user_name", "users.password", "usergroups.user_group_name")
    having = {"user_name": data["user_name"], "password": data["password"]}
    return QueryBase.view_data_to_table_having_condition(select_data,"users","usergroups","user_group_id",having)

def select_user_name(data):
    select_Data = ("user_name",)
    where = {"user_name": data["user_name"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"users", where)

def select_password(data):
    select_Data = ("password",)
    where = {"password": data["password"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"users", where)