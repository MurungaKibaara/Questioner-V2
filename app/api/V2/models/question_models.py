'''Create database model to store user data'''
import psycopg2
#from psycopg2.extras import DictCursor
from flask import jsonify
from app.api.V2.models.postgres import Questioner

INIT_DB = Questioner().init_db()

class QuestionRecords():
    """ Create a model that stores users data"""

    def __init__(self):
        """initialize the database and argument variables"""
        self.database = INIT_DB

    def questions(self, question):
        """ Add a new user to all user data """

        payload = {
            "question": question
        }
        # meetup_query = """ 'SELECT * FROM meetups WHERE meetup_id = '%d'  """ %(meetup_id)
        # cur = init_db().cursor()
        #     cur.execute(meetup_query)
        #     data = cur.fetchone()

        query = """INSERT INTO questions (question) VALUES (%(question)s)"""

        cur = self.database.cursor()
        cur.execute(query, payload)
        self.database.commit()

    def get_all_questions(self):
        '''Get all questions'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""SELECT * FROM questions""")
            data = cur.fetchall()

            if data is None:
                return jsonify({"Message":"No such questions in database"})

            question_data = {
                "status": "OK",
                "Questions": data
                }, 200
            return jsonify(question_data)

        except (psycopg2.Error) as error:
            return jsonify(error)

        return jsonify({"Message":"No questions"})

    def get_one_question(self, question_id):
        '''get one question'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""  SELECT * FROM questions WHERE question_id = '%d'  """ %(question_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"Message":"No such questions in database"})

            if data is None:
                return ({"Message":"No meetup by that ID"}), 404
            return jsonify(data), 200

        except (psycopg2.Error) as error:
            return jsonify(error)
