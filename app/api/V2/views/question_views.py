'''Questions endpoints'''
import psycopg2
from flask import Blueprint, request, jsonify, make_response, json
from app.api.V2.models.question_models import QuestionRecords
from app.api.V2.utils.validators import login_required
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

POSTQUESTION = Blueprint('post_questions', __name__)
GETQUESTIONS = Blueprint('get_question', __name__)
VOTE = Blueprint('votes', __name__)

QUESTION_RECORDS = QuestionRecords()


@POSTQUESTION.route('<int:meetup_id>/questions', methods=['POST'])
@login_required
def post_questions(meetup_id):
    '''Allow users to post questions'''
    question = request.get_json()["question"]

    cur = INIT_DB.cursor()
    cur.execute(""" SELECT question FROM questions WHERE question = '%s' """ % (question))

    data = cur.fetchone()

    if data is not None:
        return jsonify({"Message": "Question already exists"}), 400

    if not question.strip():
        return jsonify({"Error":"question field cannot be empty"}), 401

    try:
        data = QUESTION_RECORDS.questions(question, meetup_id)
        print(data)
        return make_response(jsonify({
            "status": "201",
            # "data": data,
            "message": "Success! Question posted"}), 201)

    except (psycopg2.Error) as error:
        print(error)
        return jsonify({"Error":"Programming error!"})

@GETQUESTIONS.route('/questions/all', methods=['GET'])
def getall():
    '''Allow users to get all question'''
    return QUESTION_RECORDS.get_all_questions()


@GETQUESTIONS.route('/questions/all/<int:question_id>/', methods=['GET'])
def getone(question_id):
    '''Allow users to get one question'''
    return QUESTION_RECORDS.get_one_question(question_id)

@VOTE.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
def upvote(question_id):
    '''Upvote a question'''
    return QUESTION_RECORDS.up_vote(question_id)
