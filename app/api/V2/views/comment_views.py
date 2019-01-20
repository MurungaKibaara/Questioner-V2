'''Questions endpoints'''
import psycopg2
from flask import Blueprint, request, jsonify, make_response
from app.api.V2.models.comments_model import CommentRecords
from app.api.V2.utils.validators import login_required

POSTCOMMENTS = Blueprint('post_comments', __name__)
GETCOMMENTS = Blueprint('get_comments', __name__)

COMMENT_RECORDS = CommentRecords()

@POSTCOMMENTS.route('/comments', methods=['POST'])
@login_required
def post_comments():
    '''Allow users to post questions'''
    data = request.get_json()
    comment = data["comment"]

    try:
        result = COMMENT_RECORDS.comments(comment)

        return make_response(jsonify({
            "status": "201",
            "message": "success",
            "User info": result}), 201)
    except (psycopg2.Error) as error:
        return jsonify(error)


@GETCOMMENTS.route('/comments/all', methods=['GET'])
def getall():
    '''Allow users to get all comments'''
    return COMMENT_RECORDS.get_all_comments()

@GETCOMMENTS.route('/comments/all/<int:comment_id>', methods=['GET'])
def getone(comment_id):
    '''Allow users to get one question'''
    return COMMENT_RECORDS.get_one_comment(comment_id)
