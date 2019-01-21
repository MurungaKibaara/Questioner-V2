'''Create user registration and user login endpoints'''
import re
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, make_response
from app.api.V2.models.user_models import UserRecords, login_users
from app.api.V2.models.postgresqldatabase import init_db

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
    role = "user"
    phonenumber = data["phonenumber"]
    pwd = data["password"]
    password = generate_password_hash(pwd)
    confirm_password = data["confirm_password"]
    imagefile = data["imagefile"]

    # Check whether a user exists
    cur = init_db().cursor()
    cur.execute("""  SELECT email FROM users WHERE email = '%s' """ % (email))
    data = cur.fetchone()

    if data is not None:
        return jsonify({"Message": "User already exists"}), 403

    if not firstname.strip():
        return jsonify({"Error":"firstname cannot be empty"}), 401

    if not lastname.strip():
        return jsonify({"Error":"lastname cannot be empty"}), 401

    if not phonenumber.strip():
        return jsonify({"Error":"phonenumber cannot be empty"}), 401

    if not email.strip():
        return jsonify({"Error":"email cannot be empty"}), 401

    if not password.strip():
        return jsonify({"Error":"password cannot be empty"}), 401

    if not confirm_password.strip():
        return jsonify({"Error":"confirm password cannot be empty"}), 401

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return jsonify({"error":"input valid email"})

    if not check_password_hash(password, confirm_password):
        return jsonify({"Error":"passwords did not match"}), 401


    try:
        USER_RECORDS.user_registration(firstname, lastname, email, password,
                                       confirm_password, phonenumber, role, imagefile)

        return make_response(jsonify({
            "status": "201",
            "Success": "User created"}), 201)

    except (psycopg2.Error) as error:
        return jsonify(error)


@LOGIN.route('/login', methods=['POST'])
def login():
    '''Allow users to log in'''
    return login_users()
