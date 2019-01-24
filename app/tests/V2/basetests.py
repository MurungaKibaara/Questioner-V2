'''Base test class for tests'''
import unittest
import json
#import pytest
from app import create_app
from app.api.V2.models.postgres import init_db

INIT_DB = init_db()

class BaseTest(unittest.TestCase):
    """Unittests for version 2"""

    def setUp(self):
        """Set up test variables"""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app
        self.app.testing = True
        self.database = INIT_DB


        # User signup data
        self.signup_data = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "074321234",
            "email": "ephykibrwwwa@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }

        self.signup_data1 = {
            "firstname": "",
            "lastname": "Kibaara",
            "phonenumber": "martial",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data2 = {
            "firstname": "Ephy",
            "lastname": "",
            "phonenumber": "martial",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data3 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data4 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "martial",
            "email": "",
            "password": "",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data5 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "martial",
            "email": "ephykibrwwwwwwwwwwwwwagmail.com",
            "password": "WAssup2345",
            "confirm_password": "",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data6 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "martial",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "ssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data7 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "martial",
            "email": "ephykibaara@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": ""
        }

        self.duplicate_user_data = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "martial",
            "email": "ephykibaara@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }

        # User login data

        self.login_data = {
            "email": "ephykibrwwwa@gmail.com",
            "password": "WAssup2345"
        }

        # Question data

        self.question_data = {
            "question": "What is tensorflow.js"
        }
        self.empty_question_field = {
            "question": " "
        }

        # Meetup data

        self.meetup_data = {
            "meetup_date": "28th January 2019",
            "location": "Roysambu",
            "about": "Andela bootcamp",
            "meetup_image": "image.png",
            "meetup_title": "Software development"
        }

    def registration(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data),
            content_type='application/json')
        return res

    def login(self):
        """login a registered user"""

        res = self.client.post(
            '/api/V2/login',
            data=json.dumps(self.login_data),
            content_type='application/json')
        return res

   # Tests involving meetups

    def user_token(self):
        '''Create user token'''
        user_resp = self.login()
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\")
        result = json.loads(user_resp.data.decode('utf-8'))
        token = result["token"]
        header = {"Authorization": token}
        print(header)
        return header

    def create_meetup(self):
        '''Create a meetup'''
        header = self.user_token()

        res = self.client.post(
            '/api/V2/meetups', headers=header,
            data=json.dumps(self.meetup_data), content_type='application/json')

        return res

    def get_all_meetups(self):
        '''Get all meetups'''

        res = self.client.get(
            '/api/V2/meetups/all')
        return res

    def get_one_meetup(self):
        '''get a specific meetup'''

        res = self.client.get(
            '/api/V2/meetups/all/1')
        return res

    def get_meetup_doesnt_exist(self):
        '''Test for non existent meetup'''

        res = self.client.get(
            '/api/V2/meetups/100')
        return res

    # Tests involving questions

    def post_question(self):
        """post question"""

        user_resp = self.client.post(
            '/api/V2/login',
            data=json.dumps(self.login_data),
            content_type='application/json')

        result = json.loads(user_resp.data.decode('utf-8'))
        token = ('Bearer ' + result["token"])
        header = {"Authorization": token}

        res = self.client.post(
            '/api/V2/questions', headers=header,
            data=json.dumps(self.question_data), content_type='application/json')
        return res

    def post_empty_question_field(self):
        '''Test for empty field in question'''

        res = self.client.post(
            '/api/V2/questions',
            data=json.dumps(self.empty_question_field),
            content_type='application/json')
        return res

    def get_all_questions(self):
        '''Get all questions'''

        res = self.client.get(
            '/api/V2/questions/all')
        return res

    def get_one_question(self):
        '''get a specific question'''

        res = self.client.get(
            '/api/V2/questions/all/1')
        return res

    # Tests involving comments

    def post_comments(self):
        '''Post a comment'''

        res = self.client.post(
            '/api/V2/comments',
            data=json.dumps(self.question_data),
            content_type='application/json')
        return res

    def get_all_comments(self):
        '''Get all questions'''

        res = self.client.get(
            '/api/V2/questions/all')
        return res

    def get_one_comment(self):
        '''get a apecific question'''

        res = self.client.get(
            '/api/V2/questions/all/1')
        return res

    # def tearDown(self):
    #     """Method to destroy test database tables"""
    #     destroy_tables()
