'''Create database model to store user data'''
import psycopg2
from flask import jsonify
from app.api.V2.models.postgres import Questioner

INIT_DB = Questioner().init_db()


class MeetupRecords():
    """ Create a model that stores users data"""

    def __init__(self):
        """initialize the database and argument variables"""
        self.database = INIT_DB

    def meetups(self, meetup_date, about, meetup_title, location, meetupimage):
        """ Add a new user to all user data """

        payload = {
            "meetup_title": meetup_title,
            "meetup_date":meetup_date,
            "about": about,
            "location": location,
            "meetupimage": meetupimage,
        }
        query = """INSERT INTO meetups (meetup_date, about, meetup_title, location, meetup_image)
        VALUES (%(meetup_title)s, %(about)s,%(location)s, %(meetup_date)s, %(meetupimage)s);"""

        cur = self.database.cursor()
        cur.execute(query, payload)
        self.database.commit()

    def get_all_meetups(self):
        '''Get all meetups'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""SELECT * FROM meetups;""")
            data = cur.fetchall()

            meetup_data = {
                "status": "200",
                "Meetups": data
            }, 200
            return jsonify(meetup_data)

        except psycopg2.Error as error:
            return jsonify(error)

        return "No Meetups"

    def get_one_meetup(self, meetup_id):
        '''get one question'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""  SELECT * FROM meetups WHERE meetup_id = '%d'  """ %(meetup_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"Message":"No meetup by that ID"}), 404
            return jsonify(data), 200

        except (psycopg2.Error) as error:
            return jsonify(error)

        return jsonify({"Message": "No meetups in database"}), 404

    def rsvp_a_meetup(self):
        '''RSVP MEETUP'''
        return "Hello"
