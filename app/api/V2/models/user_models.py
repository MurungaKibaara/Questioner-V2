'''Create database model to store user data'''
from app.api.V2.models.postgresqldatabase import init_db


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
            "imagefile": imagefile,
        }

        query = """INSERT INTO users_database (firstname, lastname, email, password, confirm_password, imagefile) VALUES (%(firstname)s, %(lastname)s, %(email)s,%(password)s, %(confirm_password)s, %(imagefile)s);"""
        try:
            cur = self.database.cursor()
            cur.execute(query, payload)
            self.database.commit()
        except:
            pass

    def get_users(self):
        '''Get registered user data'''
        dbconn = self.database
        cur = dbconn.cursor()
        cur.execute("""SELECT userid, email, password FROM users;""")
        data = cur.fetchall()
        response = []

        for users in enumerate(data):
            userid, email, password = users

            user_data = dict(
                userid=int(userid),
                email=email,
                password=password
            )
            response.append(user_data)

            return response
