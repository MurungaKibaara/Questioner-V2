'''Questions endpoints'''
import re
import psycopg2
from flask import Blueprint, request, jsonify
from app.api.V2.models.question_models import QuestionRecords
from app.api.V2.utils.validators import login_required
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

POSTQUESTION = Blueprint('post_questions', __name__)
GETQUESTIONS = Blueprint('get_question', __name__)
VOTE = Blueprint('votes', __name__)

QUESTION_RECORDS = QuestionRecords()


@POSTQUESTION.route('/questions', methods=['POST'])
@login_required
def post_questions():
    '''Allow users to post questions'''
    try:

        question = request.get_json()["question"]
        votes = 0

        if not question.strip():
            return jsonify({"error":"question field cannot be empty"}), 400

        if not re.match(r"^[A-Za-z][a-zA-Z]", question):
            return jsonify({"error":"input valid question"}), 400

        cur = INIT_DB.cursor()
        cur.execute(""" SELECT question FROM questions WHERE question = '%s' """ % (question))

        data = cur.fetchone()

        if data is not None:
            return jsonify({"message": "question already exists"}), 400

        try:
            return QUESTION_RECORDS.questions(question, votes)

        except (psycopg2.Error) as error:
            print(error)
            return jsonify({"error":"Programming error!"})
    except KeyError:
        return jsonify({"error":"a key is missing"})

@GETQUESTIONS.route('/questions', methods=['GET'])
def getall():
    '''Allow users to get all question'''
    return QUESTION_RECORDS.get_all_questions()


@GETQUESTIONS.route('/questions/<int:question_id>/', methods=['GET'])
def getone(question_id):
    '''Allow users to get one question'''
    return QUESTION_RECORDS.get_one_question(question_id)

@VOTE.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
def upvote(question_id):
    '''Upvote a question'''
    return QUESTION_RECORDS.up_vote(question_id)

@VOTE.route('/questions/<int:question_id>/downvote', methods=['PATCH'])
def downvote(question_id):
    '''Upvote a question'''
    return QUESTION_RECORDS.down_vote(question_id)
