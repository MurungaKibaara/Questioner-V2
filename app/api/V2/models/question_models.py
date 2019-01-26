'''Create database model to store user data'''
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import jsonify
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

class QuestionRecords():
    """ Create a model that stores users data"""

    def __init__(self):
        """initialize the database and argument variables"""
        self.database = INIT_DB

    def questions(self, question):
        """ Add a new user to all user data """

        payload = {
            "question": question,
            "votes": 0
        }

        try:
            cur = init_db().cursor()
            query = """ INSERT INTO questions (question) VALUES ('%s') """ %(question)
            cur.execute(query, payload)
            init_db().commit()

            return jsonify({
                "status": 201,
                "message":"question successfully posted"}), 201

        except psycopg2.Error as error:
            print(error)
            return jsonify({"error": "question could not be posted: database error"}), 400

    def get_all_questions(self):
        '''Get all questions'''
        try:
            cur = INIT_DB.cursor(cursor_factory=RealDictCursor)
            cur.execute("""SELECT * FROM questions""")
            data = cur.fetchall()

            if data is None:
                return jsonify({"Message":"No questions in database for this meetup"}), 404

            question_data = {
                "Status": 200,
                "questions": data
                }, 200
            return jsonify(question_data)

        except psycopg2.Error:
            return jsonify({"Error":"Could not get any question : Database error"}), 400

        return jsonify({"Message":"No questions"})

    def get_one_question(self, question_id):
        '''get one question'''
        try:
            cur = INIT_DB.cursor(cursor_factory=RealDictCursor)
            cur.execute(""" SELECT * FROM questions WHERE question_id = '%d' """ %(question_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"message":"No such questions in database"}), 404

            if data is None:
                return ({"message":"No meetup by that ID"}), 404
            return jsonify(
                {"status": 200},
                data), 200

        except psycopg2.Error:
            return jsonify({"error":"error retrieving data from database"}), 400

    def up_vote(self, question_id):
        '''A user can upvote'''
        cur = INIT_DB.cursor()
        cur.execute(
            """  SELECT votes FROM questions WHERE question_id = '%d' """ % (question_id))
        data = cur.fetchone()

        if data is None:
            return jsonify({"message": "No questions found"}), 404
        try:
            vote = data[0] + 1
            upvote_query = """ UPDATE questions SET votes = %d WHERE question_id = '%d' """ %(vote, question_id)
            cur = self.database.cursor()
            cur.execute(upvote_query)
            self.database.commit()

            return jsonify({
                "status": 200,
                "message": "successfully upvoted"
            }), 200

        except psycopg2.Error:
            return jsonify({"error":"not upvoted"}), 400

    def down_vote(self, question_id):
        '''A user can upvote'''
        try:
            cur = INIT_DB.cursor()
            cur.execute(
                """  SELECT votes FROM questions WHERE question_id = '%d' """ % (question_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"message": "No questions found"}), 404

            vote = data[0] - 1
            downvote_query = """ UPDATE questions SET votes = %d WHERE question_id = '%d' """ %(vote, question_id)
            cur = self.database.cursor()
            cur.execute(downvote_query)
            self.database.commit()

            return jsonify({
                "status": 200,
                "message": "successfully upvoted"
            }), 200

        except psycopg2.Error:
            return jsonify({"error":"not downvoted"}), 400
