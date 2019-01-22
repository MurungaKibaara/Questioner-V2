'''Questions endpoints'''
import psycopg2
from flask import Blueprint, request, jsonify, make_response
from app.api.V2.models.question_models import QuestionRecords
from app.api.V2.utils.validators import login_required
from app.api.V2.models.postgres import Questioner

INIT_DB = Questioner().init_db()

POSTQUESTION = Blueprint('post_questions', __name__)
GETQUESTIONS = Blueprint('get_question', __name__)

QUESTION_RECORDS = QuestionRecords()


@POSTQUESTION.route('/questions', methods=['POST'])
@login_required
def post_questions():
    '''Allow users to post questions'''
    question = request.get_json()["question"]

    cur = INIT_DB.cursor()
    cur.execute("""  SELECT question FROM questions WHERE question = '%s' """ % (question))
    data = cur.fetchone()

    if data is not None:
        return jsonify({"Message": "Question already exists"}), 403

    if not question.strip():
        return jsonify({"Error":"question field cannot be empty"}), 401

    try:
        QUESTION_RECORDS.questions(question)

        return make_response(jsonify({
            "status": "201",
            "message": "success! Question posted"}), 201)

    except (psycopg2.Error) as error:
        return jsonify(error)

@GETQUESTIONS.route('/questions/all', methods=['GET'])
def getall():
    '''Allow users to get all question'''
    return QUESTION_RECORDS.get_all_questions()


@GETQUESTIONS.route('/questions/all/<int:question_id>/', methods=['GET'])
def getone(question_id):
    '''Allow users to get one question'''
    return QUESTION_RECORDS.get_one_question(question_id)
