'''Create user registration and user login endpoints'''
import re
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify, make_response
from app.api.V2.models.user_models import UserRecords, login_users
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

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

    if not firstname.strip():
        return jsonify({"error":"firstname cannot be empty"}), 401

    if not re.match(r"^[A-Za-z][a-zA-Z]", firstname):
        return jsonify({"error":"input valid firstname"}), 400

    if not lastname.strip():
        return jsonify({"error":"lastname cannot be empty"}), 401

    if not re.match(r"^[A-Za-z][a-zA-Z]", lastname):
        return jsonify({"error":"input valid lastname"}), 400

    if not phonenumber.strip():
        return jsonify({"error":"phonenumber cannot be empty"}), 401

    if not re.match(r"^[0-9]", phonenumber):
        return jsonify({"error":"input valid phonenumber"}), 400

    if not email.strip():
        return jsonify({"error":"email cannot be empty"}), 401

    if not password.strip():
        return jsonify({"error":"password cannot be empty"}), 401

    if not re.match(r'[A-Za-z0-9@#$]{6,12}', pwd):
        return jsonify({"error":"Input a stronger password"}), 401

    if not confirm_password.strip():
        return jsonify({"error":"confirm password cannot be empty"}), 401

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return jsonify({"error":"input valid email"}), 400

    if not check_password_hash(password, confirm_password):
        return jsonify({"error":"passwords did not match"}), 401

    # Check whether a user exists
    cur = INIT_DB.cursor()
    cur.execute("""  SELECT email FROM users WHERE email = '%s' """ % (email))
    data = cur.fetchone()

    if data is not None:
        return jsonify({"message": "User already exists"}), 400


    try:
        USER_RECORDS.user_registration(firstname, lastname, email, password,
                                       confirm_password, phonenumber, role, imagefile)

        return make_response(jsonify({
            "status": "201",
            "success": "user created"}), 201)

    except (psycopg2.Error) as error:
        return jsonify(error)


@LOGIN.route('/login', methods=['POST'])
def login():
    '''Allow users to log in'''
    return login_users()
