'''Create database model to store user data'''
import psycopg2
from psycopg2.extras import DictCursor
from flask import jsonify
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

class QuestionRecords():
    """ Create a model that stores users data"""

    def __init__(self):
        """initialize the database and argument variables"""
        self.database = INIT_DB

    def questions(self, question, meetup_id):
        """ Add a new user to all user data """

        meetup_query = """ SELECT * FROM meetups WHERE meetup_id = '%d'  """ %(meetup_id)
        cur = INIT_DB.cursor()
        cur.execute(meetup_query)
        data = cur.fetchone()
        print(data)

        if data is None:
            return jsonify({"message":"No Meetup by that ID"})

        payload = {
            "question": question,
            "votes":0
        }
        print(payload["question"])
        try:
            cur = init_db().cursor()
            query = """ INSERT INTO questions (question) VALUES ''%s;""" %(question)
            cur.execute(query, payload)
            init_db().commit()

        except:
            return jsonify({"error": "question could not be posted"})

    def get_all_questions(self):
        '''Get all questions'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""SELECT * FROM questions""")
            data = cur.fetchall()

            if data is None:
                return jsonify({"Message":"No questions in database for this meetup"})

            question_data = {
                "Status": "OK",
                "Questions": data
                }, 200
            return jsonify(question_data)

        except (psycopg2.Error) as error:
            print(error)
            return jsonify({"Error":"Could not get any question : programming error"})

        return jsonify({"Message":"No questions"})

    def get_one_question(self, question_id):
        '''get one question'''
        try:
            cur = INIT_DB.cursor()
            cur.execute(""" SELECT * FROM questions WHERE question_id = '%d' """ %(question_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"Message":"No such questions in database"})

            if data is None:
                return ({"Message":"No meetup by that ID"}), 404
            return jsonify(data), 200

        except (psycopg2.Error) as error:
            return jsonify(error)

    def up_vote(self, question_id):
        '''A user can upvote'''
        cur = INIT_DB.cursor()
        cur.execute(
            """  SELECT votes FROM questions WHERE question_id = '%d' """ % (question_id))
        data = cur.fetchone()

        if data is None:
            return jsonify({"Message": "No data here"})

        vote = data[0] + 1
        upvote_query = """ UPDATE questions SET votes = %d """ %(vote)
        cur = self.database.cursor()
        cur.execute(upvote_query)
        self.database.commit()

        for question in data:
            return jsonify(question)

        return "Not upvoted"
