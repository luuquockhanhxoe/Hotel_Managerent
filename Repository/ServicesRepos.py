from Repository import QueryBase

def select_all_services():
    select_Data = ("*",)
    return QueryBase.view_data_to_table(select_Data, "services")

def select_one_services(id):
    select_Data = ("*",)
    where = {"service_id": id}
    return QueryBase.view_data_to_table_conditions(select_Data,"services", where)

def select_service(data):
    select_Data = ("service_name",)
    where = {"service_name": data["service_name"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"services", where)

def insert_service(data):
    columns = {"service_name": data["service_name"],
               "service_price": data["service_price"]}
    return QueryBase.add_data_to_table("services", columns)

def update_service(id,data):
    update_column = {"service_name": data['service_name'],
                     "service_price": data["service_price"]}
    where = {"service_id": id}
    return QueryBase.update_data_to_table("services",update_column, where)

def delete_service(id):
    where = {"service_id": id}
    return QueryBase.delete_data_to_table_conditions("services", where)
