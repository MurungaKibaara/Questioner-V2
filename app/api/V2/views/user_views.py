'''Create user registration and user login endpoints'''
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, make_response
from app.api.V2.models.user_models import UserRecords
from app.api.V2.models.user_models import RESPONSE

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

    try:
        result = USER_RECORDS.user_registration(firstname, lastname,
                                                email, password, confirm_password, imagefile)

        return make_response(jsonify({
            "status": "201",
            "message": "success",
            "User info": result}), 201)
    except (psycopg2.Error) as error:
        return jsonify(error)


@LOGIN.route('/login', methods=['POST', 'GET'])
def login():
    '''Allow users to log in'''
    data = request.get_json()

    email = data["email"]
    password = data["password"]

    for user_data in RESPONSE:
        if email == user_data['email'] and check_password_hash(password, user_data['password']):

            return make_response(jsonify({
                "status": "200",
                "message": "successfully logged in",
                "Logged in as ": user_data["email"]}), 200)

        return make_response(jsonify({"status": "404", "message": "User doesn't exist"}), 404)
    return make_response(jsonify({"status": "404", "message": "No data in database"}), 404)
