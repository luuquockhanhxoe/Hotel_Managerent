from Repository import QueryBase

def select_all_customers():
    select_Data = ("*",)
    return QueryBase.view_data_to_table(select_Data, "customers")

def select_one_customers(id):
    select_Data = ("*",)
    where = {"customer_id": id}
    return QueryBase.view_data_to_table_conditions(select_Data,"customers", where)

def select_customer(data):
    select_Data = ("*",)
    where = {"full_name": data["full_name"], "phone": data["phone"]}
    return QueryBase.view_data_to_table_conditions(select_Data,"customers", where)

def insert_customer(data):
    columns = {"full_name": data["full_name"], "phone": data["phone"]}
    return QueryBase.add_data_to_table("customers", columns)

def update_customer(id,data):
    update_column = {"full_name": data["full_name"], "phone": data["phone"]}
    where = {"customer_id":id}
    return QueryBase.update_data_to_table("customers",update_column, where)

def delete_customer(id):
    where = {"customer_id": id}
    return QueryBase.delete_data_to_table_conditions("customers", where)
