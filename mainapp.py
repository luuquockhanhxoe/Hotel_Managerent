from flask import Flask
from flask_restful import Api, Resource
from Handler.UsersAPI import usersApi
from Handler.UserGroupsAPI import userroupsApi
from Handler.HotelGroupsAPI import hotelgroupsApi
from Handler.ServicesAPI import servicesApi
from Handler.HotelRoomAPI import hotelroomsAPI
from Handler.LoginAPI import loginApi
from Handler.CustomerAPI import customersApi

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(loginApi)
    app.register_blueprint(servicesApi)
    app.register_blueprint(userroupsApi)
    app.register_blueprint(usersApi)
    app.register_blueprint(hotelroomsAPI)
    app.register_blueprint(hotelgroupsApi)
    app.register_blueprint(customersApi)
    app.run(debug=True)