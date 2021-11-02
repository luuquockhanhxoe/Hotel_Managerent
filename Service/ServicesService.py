from Repository import ServicesRepos
from flask import jsonify


def show_all_services():
    services = ServicesRepos.select_all_services()
    try:
        output = []
        for service in services:
            service = {'service_id': service['service_id'],
                       'service_name': service['service_name'],
                       'service_price': service['service_price']}
            output.append(service)
        return jsonify({"services": output})
    except:
        return jsonify({"message": "Không có service nào cả!"})


def add_services_to_data(data):
    check_data = ServicesRepos.select_service(data)
    if check_data:
        return jsonify({"message": "Đã tồn tại service name này!", 
                        "service": check_data})
    else: 
        ServicesRepos.insert_service(data)
        service = ServicesRepos.select_service(data)
        return jsonify({"message": "Thêm thành công",
                        "service": service})


def change_services(id,data):
    check_data = ServicesRepos.select_service(data)
    if check_data:
        ServicesRepos.update_service(id,data)
        service = ServicesRepos.select_service(data)
        return jsonify({"message": "Đổi service thành công",
                        "service": service})
    else :
        return jsonify({"message": "Đã tồn tại service name này!",
                        "service": check_data})


def delete_services(data):
    ServicesRepos.delete_service(data)
    return jsonify({"message": "Xóa service thành công"})

def show_one_services(id):
    service = ServicesRepos.select_one_services(id)
    try:
        service_data = {'service_id': service['service_id'],
                        'service_name': service['service_name'],
                        'service_price': service['service_price']}
        return jsonify({"service": service_data})
    except:
        return jsonify({"message": "Không có service id này!"})
