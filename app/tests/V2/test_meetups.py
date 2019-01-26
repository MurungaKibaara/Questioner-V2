'''Test Meetups'''
from .basetests import BaseTest

class TestMeetups(BaseTest):
    '''Test all meetups'''

    def test_create_meetup(self):
        '''Test create meetup endpoint'''
        self.registration()
        response = self.create_meetup()
        self.assertEqual(response.status_code, 201)

    def test_get_all_meetups(self):
        '''Test get all meetups endpoint'''
        self.registration()
        self.create_meetup()
        response = self.get_all_meetups()
        self.assertEqual(response.status_code, 200)

    def test_get_meetup(self):
        '''Test get specific meetup endpoint'''
        self.registration()
        self.create_meetup()
        response = self.get_all_meetups()
        self.assertEqual(response.status_code, 200)

    def test_meetup_does_not_exist(self):
        '''Test get nonexistent meetup'''
        response = self.get_meetup_doesnt_exist()
        self.assertEqual(response.status_code, 404)

    def test_missing_location(self):
        """Test missing field"""
        response = self.missing_meetup_location()
        self.assertEqual(response.status_code, 400)

    def test_missing_title(self):
        """Test missing field"""
        response = self.missing_meetup_title()
        self.assertEqual(response.status_code, 400)

    def test_missing_about(self):
        """Test missing field"""
        response = self.missing_meetup_about()
        self.assertEqual(response.status_code, 400)

    def test_missing_meetup_date(self):
        """Test missing field"""
        response = self.missing_meetup_date()
        self.assertEqual(response.status_code, 400)
