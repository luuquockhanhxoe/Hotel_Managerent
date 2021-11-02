from Repository import UsersRepos
from Handler import UsersAPI
from flask import jsonify


def show_all_users():
    users = UsersRepos.select_all_users()
    try:
        output = []
        for user in users:
            user = {'user_id': user['user_id'],
                    'user_name': user['user_name'],
                    'passsword': user['passsword'],
                    'user_group_id': user['user_group_id']}
            output.append(user)
        return jsonify({"users": output})
    except:
        return jsonify({"message": "Không có user nào cả!"})


def add_users_to_data(data):
    check_data = UsersRepos.select_user(data)
    if check_data:
        return jsonify({"message": "Đã tồn tại user name này!", 
                        "user": check_data})
    else: 
        UsersRepos.insert_user(data)
        user = UsersRepos.select_user(data)
        return jsonify({"message": "Thêm thành công",
                        "user": user})


def change_users(id,data):
    check_data = UsersRepos.select_user(data)
    if check_data:
        UsersRepos.update_user(id,data)
        user = UsersRepos.select_user(data)
        return jsonify({"message": "Đổi dũ liệu user thành công",
                        "user": user})
    else :
        return jsonify({"message": "Đã tồn tại user name này!",
                        "user": check_data})

def delete_users(id):
    UsersRepos.delete_user(id)
    return jsonify({"message": "Xóa user thành công"})

def show_one_users(id):
    user = UsersRepos.select_one_users(id)
    try:
        user = {'user_id': user['user_id'],
                'user_name': user['user_name'],
                'passsword': user['passsword'],
                'user_group_id': user['user_group_id']}
        return jsonify({"user": user})
    except:
        return jsonify({"message": "Không có user id này!"})
