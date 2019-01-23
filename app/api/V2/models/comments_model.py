'''Create database model to store user data'''
import psycopg2
from flask import jsonify
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

class CommentRecords():
    """ Create a model that stores users data"""

    def __init__(self):
        """initialize the database and argument variables"""
        self.database = INIT_DB

    def comments(self, comment):
        """ Add a new user to all user data """

        payload = {
            "comment": comment
        }

        query = """INSERT INTO comments (comment) VALUES (%(comment)s)"""

        cur = self.database.cursor()
        cur.execute(query, payload)
        self.database.commit()

    def get_all_comments(self):
        '''Retrieve all comments'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""SELECT * FROM comments;""")
            data = cur.fetchall()

            if data is None:
                return jsonify({"message":"No comment by that id"})

            comment_data = {
                "status": "OK",
                "Comments": data
                }, 200
            return jsonify(comment_data)

        except (psycopg2.Error) as error:
            return jsonify(error)

        return jsonify({"message":"No comments avaailable for this question"})

    def get_one_comment(self, comment_id):
        '''Retrieve one comment'''
        try:
            cur = INIT_DB.cursor()
            cur.execute("""  SELECT * FROM comments WHERE comment_id = '%d'  """ %(comment_id))
            data = cur.fetchone()

            if data is None:
                return jsonify({"message":"No comment by that id"})

            if data is None:
                return ({"Message":"No Comment by that ID"}), 404
            return jsonify(data), 200

        except (psycopg2.Error) as error:
            return jsonify(error)
