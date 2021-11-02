from Repository import CustomersRepos
from Handler import CustomerAPI
from flask import jsonify


def show_all_customers():
    customers = CustomersRepos.select_all_customers()
    try:
        output = []
        for customer in customers:
            customer = {'customer_id': customer['customer_id'],
                         'full_name': customer['full_name'],
                         'phone': customer['phone']}

            output.append(customer)
        return jsonify({"customers": output})
    except:
        return jsonify({"message": "Không có customer nào cả!"})


def add_customers_to_data(data):
    CustomersRepos.insert_customer(data)
    customers_id = CustomersRepos.select_customer(data)
    return jsonify({"message": "Thêm thành công",
                    "customer": customers_id})

def change_customers(id,data):

    CustomersRepos.update_customer(id,data)
    customer = CustomersRepos.select_customer(data)
    return jsonify({"message": "Đổi tên customer thành công",
                    "customer": customer})

def delete_customers(id):
    CustomersRepos.delete_customer(id)
    return jsonify({"message": "Xóa customer thành công"})

def show_one_customers(id):
    customer = CustomersRepos.select_one_customers(id)
    try:
        data = {'customer_id': customer['customer_id'],
                         'full_name': customer['full_name'],
                         'phone': customer['phone']}
        return jsonify({"customer": data})
    except:
        return jsonify({"message": "Không có customer id này!"})