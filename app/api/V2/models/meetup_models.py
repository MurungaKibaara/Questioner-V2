'''Create database model to store user data'''
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import jsonify
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

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

        try:
            cur = self.database.cursor()
            cur.execute(query, payload)
            self.database.commit()

            return jsonify({"message":"meetup posted successfully"}), 201

        except psycopg2.Error:
            return jsonify({"error":"Could not post meetups"}), 400

    def get_all_meetups(self):
        '''Get all meetups'''
        try:
            cur = INIT_DB.cursor(cursor_factory=RealDictCursor)
            cur.execute("""SELECT * FROM meetups;""")
            data = cur.fetchall()

            meetup_data = {
                "status": "200",
                "Meetups": data
            }, 200

            return jsonify(meetup_data)

        except psycopg2.Error:
            return jsonify({"error":"error posting meetups:database error"}), 400

        return jsonify({"error": "No meetups in database"}), 404

    def get_one_meetup(self, meetup_id):
        '''get one question'''
        try:
            cur = INIT_DB.cursor(cursor_factory=RealDictCursor)
            cur.execute("""  SELECT * FROM meetups WHERE meetup_id = '%d'  """ %(meetup_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"Message":"No meetup by that ID"}), 404
            return jsonify(data), 200

        except psycopg2.Error:
            return jsonify({"error":"no question returned: database error"})

        return jsonify({"Message": "No meetups in database"}), 404

    def rsvp_a_meetup(self):
        '''RSVP MEETUP'''
        return "Hello"
