'''Test Meetups'''
from .basetests import BaseTest

class TestMeetups(BaseTest):
    '''Test all meetups'''

    def test_create_meetup(self):
        '''Test create meetup endpoint'''
        response = self.create_meetup()
        self.assertEqual(response.status_code, 201)

    def test_get_all_meetups(self):
        '''Test get all meetups endpoint'''
        self.create_meetup()
        response = self.get_all_meetups()
        self.assertEqual(response.status_code, 200)

    def test_get_meetup(self):
        '''Test get specific meetup endpoint'''
        response = self.get_all_meetups()
        self.assertEqual(response.status_code, 200)

    def test_meetup_does_not_exist(self):
        '''Test get nonexistent meetup'''
        response = self.get_meetup_doesnt_exist()
        self.assertEqual(response.status_code, 404)
