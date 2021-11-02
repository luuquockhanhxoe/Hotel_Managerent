from flask import request
from flask import json
from Service import Authentication
from flask import Blueprint
loginApi = Blueprint("loginApi", __name__)


@loginApi.route('/login', methods = ['POST'])
def welcome():
    data = request.json
    return Authentication.login(data)