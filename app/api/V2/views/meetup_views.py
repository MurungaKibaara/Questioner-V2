'''Questions endpoints'''
import re
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Blueprint, request, jsonify
from app.api.V2.models.meetup_models import MeetupRecords
from app.api.V2.utils.validators import login_required
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

POSTMEETUP = Blueprint('post_meetups', __name__)
GETMEETUPS = Blueprint('get_meetups', __name__)

MEETS = MeetupRecords()

@POSTMEETUP.route('/meetups', methods=['POST'])
@login_required
def post_meetups():
    '''Allow admins to post meetups'''
    try:
        data = request.get_json()

        meetup_title = data["meetup_title"]
        about = data["about"]
        location = data["location"]
        meetup_date = data["meetup_date"]
        meetup_image = data["meetup_image"]

        if not meetup_title.strip():
            return jsonify({"error":"question field cannot be empty"}), 400

        if not re.match(r"^[A-Za-z][a-zA-Z]", meetup_title):
            return jsonify({"error":"input valid meetup_title"}), 400

        if not about.strip():
            return jsonify({"error":"about field cannot be empty"}), 400

        if not re.match(r"^[A-Za-z][a-zA-Z]", about):
            return jsonify({"error":"input valid about"}), 400

        if not location.strip():
            return jsonify({"Error":"question field cannot be empty"}), 400

        if not re.match(r"^[A-Za-z][a-zA-Z]", location):
            return jsonify({"error":"input valid location"}), 400

        if not meetup_date.strip():
            return jsonify({"error":"question field cannot be empty"}), 400

        if not meetup_image.strip():
            return jsonify({"error":"question field cannot be empty"}), 400

        try:

            cur = INIT_DB.cursor(cursor_factory=RealDictCursor)
            cur.execute("""  SELECT meetup_title FROM meetups WHERE meetup_title = '%s' """ %(meetup_title))
            data = cur.fetchone()

            if data is not None:
                return jsonify({"Message": "meetup already exists"}), 400

            return MeetupRecords().meetups(meetup_date, about, meetup_title, location, meetup_image)

        except psycopg2.Error:
            return jsonify({"error":"error posting meetups to database"}), 400

    except KeyError:
        return jsonify({"error":"A key is missing"}), 400


@GETMEETUPS.route('/meetups', methods=['GET'])
def getall():
    '''Allow users to get all meetups'''
    return MEETS.get_all_meetups()

@GETMEETUPS.route('/meetups/<int:meetup_id>', methods=['GET'])
def getone(meetup_id):
    '''Allow users to get one meetup'''
    return MEETS.get_one_meetup(meetup_id)
