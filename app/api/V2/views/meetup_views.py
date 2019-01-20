'''Questions endpoints'''
import psycopg2
from flask import Blueprint, request, jsonify
from app.api.V2.models.meetup_models import MeetupRecords
from app.api.V2.utils.validators import login_required

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

    try:
        result = MeetupRecords().meetups(meetup_date, about, meetup_title, location, meetup_image)

        return jsonify({
            "status": "201",
            "message": "success",
            "info": result}), 201
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
