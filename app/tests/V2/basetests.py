'''Base test class for tests'''
import unittest
import json
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
            "phonenumber": "0743212345",
            "email": "ephkibrwa@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }

        self.signup_data1 = {
            "firstname": "",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data2 = {
            "firstname": "Ephy",
            "lastname": "",
            "phonenumber": "0780997711",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "@WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data3 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": " ",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "@WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data4 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "",
            "password": "@WAssup2345",
            "confirm_password": "@WAssup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data5 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data8 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "",
            "confirm_password": "@Wassup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data9 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibrwwwwwwwwwwwwwagmail.com",
            "password": "@WAssup2345",
            "confirm_password": "@Wassup2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data6 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibrwwwwwwwwwwwwwa@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "ssup@2345",
            "imagefile": "imagefile.jpg"
        }
        self.signup_data7 = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibaara@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "@WAssup2345",
            "imagefile": ""
        }

        self.duplicate_user_data = {
            "firstname": "Ephy",
            "lastname": "Kibaara",
            "phonenumber": "0780997711",
            "email": "ephykibaara@gmail.com",
            "password": "@WAssup2345",
            "confirm_password": "WAssup2345",
            "imagefile": "imagefile.jpg"
        }

        # User login data

        self.login_data = {
            "email": "ephkibrwa@gmail.com",
            "password": "@WAssup2345"
        }

        # Question data

        self.question_data = {
            "question": "What is tensorflow.js"
        }
        self.empty_question_field = {
            "question": " "
        }

        # comment data

        self.comment_data = {
            "comment": "It is part of machine learning"
        }
        self.empty_comment_field = {
            "comment": " "
        }

        # Meetup data

        self.meetup_data = {
            "meetup_date": "28th January 2019",
            "location": "Roysambu",
            "about": "Andela bootcamp",
            "meetup_image": "image.png",
            "meetup_title": "Software development"
        }
        self.meetup_data1 = {
            "meetup_date": "",
            "location": "Roysambu",
            "about": "Andela bootcamp",
            "meetup_image": "image.png",
            "meetup_title": "Software development"
        }
        self.meetup_data2 = {
            "meetup_date": "28th January 2019",
            "location": "",
            "about": "Andela bootcamp",
            "meetup_image": "image.png",
            "meetup_title": "Software development"
        }
        self.meetup_data3 = {
            "meetup_date": "28th January 2019",
            "location": "Roysambu",
            "about": "",
            "meetup_image": "image.png",
            "meetup_title": "Software development"
        }
        self.meetup_data4 = {
            "meetup_date": "28th January 2019",
            "location": "Roysambu",
            "about": "Andela bootcamp",
            "meetup_image": "",
            "meetup_title": "Software development"
        }
        self.meetup_data5 = {
            "meetup_date": "28th January 2019",
            "location": "Roysambu",
            "about": "Andela bootcamp",
            "meetup_image": "image.png",
            "meetup_title": ""
        }

    def registration(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data),
            content_type='application/json')
        return res

    def missing_first_name(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data1),
            content_type='application/json')
        return res

    def missing_last_name(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data2),
            content_type='application/json')
        return res

    def missing_phone_number(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data3),
            content_type='application/json')
        return res

    def missing_email(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data3),
            content_type='application/json')
        return res

    def missing_password(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data8),
            content_type='application/json')
        return res

    def missing_image(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data7),
            content_type='application/json')
        return res

    def missing_confirm_password(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data5),
            content_type='application/json')
        return res

    def unmatched_passwords(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data6),
            content_type='application/json')
        return res

    def invalid_email(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/registration',
            data=json.dumps(self.signup_data9),
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
        result = json.loads(user_resp.data.decode('utf-8'))
        token = result["token"]
        header = {"Authorization": token}
        return header

    def create_meetup(self):
        '''Create a meetup'''
        self.registration()
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

    def missing_meetup_title(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/meetups',
            data=json.dumps(self.meetup_data5),
            content_type='application/json')
        return res

    def missing_meetup_date(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/meetups',
            data=json.dumps(self.meetup_data1),
            content_type='application/json')
        return res

    def missing_meetup_about(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/meetups',
            data=json.dumps(self.meetup_data3),
            content_type='application/json')
        return res

    def missing_meetup_location(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/meetups',
            data=json.dumps(self.meetup_data2),
            content_type='application/json')
        return res

    def missing_meetup_image(self):
        '''Register a new user'''
        res = self.client.post(
            '/api/V2/meetups',
            data=json.dumps(self.meetup_data4),
            content_type='application/json')
        return res

    # Tests involving questions

    def post_question(self):
        """post question"""
        self.registration()
        self.login()
        header = self.user_token()

        res = self.client.post(
            '/api/V2/1/questions', headers=header,
            data=json.dumps(self.question_data), content_type='application/json')
        return res

    def post_empty_question_field(self):
        '''Test for empty field in question'''
        self.registration()
        self.login()
        header = self.user_token()
        res = self.client.post(
            '/api/V2/1/questions',
            data=json.dumps(self.empty_question_field), headers=header,
            content_type='application/json')
        return res

    def get_all_questions(self):
        '''Get all questions'''

        res = self.client.get(
            '/api/V2/questions')
        return res

    def get_one_question(self):
        '''get a specific question'''
        res = self.client.get(
            '/api/V2/questions/1/')
        return res

    def get_one_question_doesnt_exist(self):
        '''get a specific question'''
        res = self.client.get(
            '/api/V2/questions/431/')
        return res

    # Tests involving comments

    def post_comments(self):
        '''Post a comment'''
        self.registration()
        header = self.user_token()

        res = self.client.post(
            '/api/V2/comments',
            data=json.dumps(self.comment_data), headers=header,
            content_type='application/json')
        return res

    def post_empty_comment_field(self):
        '''Test for empty field in question'''
        self.registration()
        self.login()
        header = self.user_token()
        res = self.client.post(
            '/api/V2/comments',
            data=json.dumps(self.empty_comment_field), headers=header,
            content_type='application/json')
        return res

    def get_all_comments(self):
        '''Get all questions'''

        res = self.client.get(
            '/api/V2/comments')
        return res

    def get_one_comment(self):
        '''get a apecific question'''

        res = self.client.get(
            '/api/V2/comments/1')
        return res

    def get_one_comment_doesnt_exist(self):
        '''get a specific question'''
        res = self.client.get(
            '/api/V2/comments/431/')
        return res

    # def tearDown(self):
    #     """Method to destroy test database tables"""
    #     destroy_tables()
