'''Create database model to store user data'''
import psycopg2
from flask import jsonify
from app.api.V2.models.postgresqldatabase import init_db
RESPONSE = []

class UserRecords():
    """ Create a model that stores users data"""

    def __init__(self):
        """initialize the database and argument variables"""
        self.database = init_db()

    def user_registration(self, firstname, lastname, email, password, confirm_password, imagefile):
        """ Add a new user to all user data """

        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
            "imagefile": imagefile
        }

        query = """INSERT INTO users (firstname, lastname, email,
        password, confirm_password, imagefile) VALUES
        (%(firstname)s, %(lastname)s, %(email)s,%(password)s,
        %(confirm_password)s, %(imagefile)s);"""

        cur = self.database.cursor()
        cur.execute(query, payload)
        self.database.commit()

    def login_users(self):
        '''Login a user'''
        try:
            cur = init_db().cursor()
            cur.execute("""SELECT * FROM users;""")
            data = cur.fetchall()

        except (psycopg2.Error) as error:
            return jsonify(error)

        for user in enumerate(data):
            email, password = user

            user_data = dict(
                email=email,
                password=password
            )
            RESPONSE.append(user_data)
        return RESPONSE
