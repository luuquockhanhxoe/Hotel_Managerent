from Model.Setting import Services
from Service import CustomersService
from flask import request
from flask import jsonify
from flask import Blueprint
customersApi = Blueprint("customersApi", __name__)


@customersApi.route('/customers', methods = ['GET'])
def get_customers():
    #lấy tất cả thông tin cơ bản của customers.
    return CustomersService.show_all_customers()

@customersApi.route('/customers', methods = ['POST'])
def post_customer():
    #thêm thông tin cơ bản của customers.
    data = request.json
    return CustomersService.add_customers_to_data(data)

@customersApi.route('/customers/<id>', methods = ['PUT'])
def put_customer(id):
    #sửa customer
    data = request.json
    return CustomersService.change_customers(id,data)


@customersApi.route('/customers/<id>', methods = ['DELETE'])
def delete_customer(id):      
#xóa customers
    data = request.json
    return CustomersService.delete_customers(id)


@customersApi.route('/customers/<id>', methods = ['GET'])
def get_customer(id):  
#lấy thông tin cơ bản của customer theo id
    return CustomersService.show_one_customers(id)
