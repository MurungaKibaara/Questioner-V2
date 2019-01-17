'''Create user registration and user login endpoints'''
from werkzeug.security import generate_password_hash
from flask import Blueprint, request, jsonify, make_response
from app.api.V2.models.user_models import UserRecords

REGISTRATION = Blueprint('user_registration', __name__)
LOGIN = Blueprint('user_login', __name__)

USER_RECORDS = UserRecords()


@REGISTRATION.route('/registration', methods=['POST'])
def user_reg():
    '''Create user registration endpoint'''
    data = request.get_json()
    firstname = data["firstname"]
    lastname = data["lastname"]
    email = data["email"]
    pwd = data["password"]
    password = generate_password_hash(pwd)
    confirm_password = data["confirm_password"]
    imagefile = data["imagefile"]


    result = USER_RECORDS.user_registration(firstname, lastname,
                                            email, password, confirm_password, imagefile)

    return make_response(jsonify({
        "status": "201",
        "message": "success",
        "User Data": result}), 201)


# @LOGIN.route('/login', methods=['POST', 'GET'])
# def user_signin():
#     '''Allow users to log in'''
#     data = request.get_json()

#     email = data["email"]
#     password = data["password"]

#     Users = UserRecords.get_users()
#     if email == Users["email"] and password == ["password"]:
#         return make_response (jsonify({
#         "status": "201",
#         "message": "success, Use logged in"
#         }), 201)
