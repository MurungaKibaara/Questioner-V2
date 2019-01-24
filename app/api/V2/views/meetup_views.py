'''Questions endpoints'''
import re
import psycopg2
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
    data = request.get_json()

    meetup_title = data["meetup_title"]
    about = data["about"]
    location = data["location"]
    meetup_date = data["meetup_date"]
    meetup_image = data["meetup_image"]

    cur = INIT_DB.cursor()
    cur.execute("""  SELECT meetup_title FROM meetups WHERE meetup_title = '%s' """ %(meetup_title))
    data = cur.fetchone()

    if data is not None:
        return jsonify({"Message": "meetup already exists"}), 400

    if not meetup_title.strip():
        return jsonify({"Error":"question field cannot be empty"}), 401

    if not re.match(r"^[A-Za-z][a-zA-Z]", meetup_title):
        return jsonify({"error":"input valid meetup_title"})

    if not about.strip():
        return jsonify({"Error":"about field cannot be empty"}), 401

    if not re.match(r"^[A-Za-z][a-zA-Z]", about):
        return jsonify({"error":"input valid about"})

    if not location.strip():
        return jsonify({"Error":"question field cannot be empty"}), 401
    if not re.match(r"^[A-Za-z][a-zA-Z]", location):
        return jsonify({"error":"input valid location"})

    if not meetup_date.strip():
        return jsonify({"Error":"question field cannot be empty"}), 401

    if not meetup_image.strip():
        return jsonify({"Error":"question field cannot be empty"}), 401


    try:
        MeetupRecords().meetups(meetup_date, about, meetup_title, location, meetup_image)

        return jsonify({
            "status": "201",
            "message": "success! Meetup posted"}), 201
    except (psycopg2.Error) as error:
        return jsonify(error)


@GETMEETUPS.route('/meetups/all', methods=['GET'])
def getall():
    '''Allow users to get all meetups'''
    return MEETS.get_all_meetups()

@GETMEETUPS.route('/meetups/all/<int:meetup_id>', methods=['GET'])
def getone(meetup_id):
    '''Allow users to get one meetup'''
    return MEETS.get_one_meetup(meetup_id)
