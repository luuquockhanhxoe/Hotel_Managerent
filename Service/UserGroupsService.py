from Repository import UserGroupsRepos
from Handler import UserGroupsAPI
from flask import jsonify


def show_all_usergroups():
    usergroups = UserGroupsRepos.select_all_usergroups()
    try:
        output = []
        for usergroup in usergroups:
            usergroup = {'user_group_id': usergroup['user_group_id'],
                         'user_group_name': usergroup['user_group_name']}

            output.append(usergroup)
        return jsonify({"usergroups": output})
    except:
        return jsonify({"message": "Không có usergroup nào cả!"})


def add_usergroups_to_data(data):
    check_data = UserGroupsRepos.select_usergroup(data)
    if check_data:
        return jsonify({"message": "Đã tồn tại username này!", 
                "user_group": check_data})
    else: 
        UserGroupsRepos.insert_user_group(data)
        user_group_id = UserGroupsRepos.select_usergroup(data)
        return jsonify({"message": "Thêm thành công",
                "usergroup": user_group_id})


def change_usergroups(id,data):
    check_data = UserGroupsRepos.select_usergroup(data)
    if check_data:
        UserGroupsRepos.update_user_group(id,data)
        user_group = UserGroupsRepos.select_usergroup(data)
        return jsonify({"message": "Đổi tên user group name thành công",
                        "usergroup": user_group})
    else :
        return jsonify({"message": "Đã tồn tại user group name này!",
                        "user_group": check_data})

def delete_usergroups(id):
    UserGroupsRepos.delete_user_group(id)
    return jsonify({"message": "Xóa user group thành công"})

def show_one_usergroups(id):
    usergroup = UserGroupsRepos.select_one_usergroups(id)
    try:
        user_data = {"user_group_name": usergroup['user_group_name']}
        return jsonify({"usergroup": user_data})
    except:
        return jsonify({"message": "Không có user group id này!"})