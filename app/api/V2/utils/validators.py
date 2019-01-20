'''Validators and decorators'''
from functools import wraps
from flask import request, jsonify
from app.api.V2.models.user_models import verify_token


def login_required(auth_function):
    '''Creates login requred decorator'''
    @wraps(auth_function)
    def decorated_function(*args, **kws):
        '''Create decorated function'''

        auth_token = None
        auth_header = request.headers.get('Authorization')

        if auth_header:
            auth_token = auth_header.split("Bearer" )[1]

        if not auth_token:
            return jsonify({"message": "Token required"}), 401
        try:
            response = verify_token(auth_token)

            if isinstance(response, str):
                user = response
                if not user:
                    return jsonify({"message": "Wrong email"}), 400
        except:
            return jsonify({"message": "Token is invalid"}), 400

        return auth_function(*args, **kws)
    return decorated_function
