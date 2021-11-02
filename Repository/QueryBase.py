from Database.ConnectSQL import connectDB
@connectDB
def add_data_to_table(mycursor,table_name_add, data):
    columns = ",".join(data.keys())
    values = ",".join(len(data)*["%s"])
    sql = "INSERT INTO `{}`({}) VALUES ({})".format(table_name_add,columns,values) 
    value_swap = [int(i) if isinstance(i, bool) else i for i in data.values()]
    return mycursor.execute(sql,value_swap)

    
@connectDB
def update_data_to_table(mycursor,table_name_add, data, conditions):
    update_value_for_keys = "= %s, ".join(data.keys())
    where_for_keys = "= %s AND ".join(conditions.keys())
    sql = "UPDATE `{}` SET {} = %s WHERE {} = %s".format(table_name_add,update_value_for_keys, where_for_keys)
    values = list(data.values())+ list(conditions.values())
    value_swap = [int(i) if isinstance(i, bool) else i for i in values]
    return mycursor.execute(sql,value_swap)


@connectDB
def view_data_to_table(mycursor,select_data, table_name):
    select_datas = ", ".join(select_data)
    sql = "SELECT {} FROM {}".format(select_datas,table_name)   
    mycursor.execute(sql)
    return mycursor.fetchall()

@connectDB
def view_data_to_table_having_condition(mycursor,select_data, table_name1, table_name2, primary, conditions):
    select_datas = ", ".join(select_data)
    having_for_keys = "= %s AND ".join(conditions.keys())
    sql = "SELECT {0} FROM {1},{2} WHERE {3}.{4}={5}.{6} HAVING {7} = %s ".format(select_datas,table_name1,table_name2,table_name1,primary,table_name2,primary,having_for_keys)
    value_swap = [int(i) if isinstance(i, bool) else i for i in conditions.values()]
    mycursor.execute(sql, value_swap)
    return mycursor.fetchone()

@connectDB
def view_data_to_table_conditions(mycursor,select_data, table_name, conditions):
    select_datas = ", ".join(select_data)
    where_for_keys = "= %s AND ".join(conditions.keys())
    sql = "SELECT {} FROM {} WHERE {} = %s".format(select_datas,table_name,where_for_keys)
    value_swap = [int(i) if isinstance(i, bool) else i for i in conditions.values()]
    mycursor.execute(sql, value_swap)
    return  mycursor.fetchone()

@connectDB
def delete_data_to_table_conditions(mycursor, table_name, conditions):
    where_for_keys = "= %s AND ".join(conditions.keys())
    sql = "DELETE FROM {} WHERE {} = %s".format(table_name,where_for_keys)
    value_swap = [int(i) if isinstance(i, bool) else i for i in conditions.values()]
    mycursor.execute(sql, value_swap)
    return mycursor.fetchone()


# gia_tri = []
# for i in a.values():
#     if isinstance(i, bool):
#         gia_tri.append(int(i))
#     else:
#         gia_tri.append(i)
