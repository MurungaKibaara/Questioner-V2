'''Tests for users'''
from .basetests import BaseTest

class TestUsers(BaseTest):
    """Test user registration and login"""

    def test_user_registration(self):
        '''Test register new account'''
        response = self.registration()
        self.assertEqual(response.status_code, 201)


    def test_user_login(self):
        """Test user login endpoint"""
        response = self.login()
        self.assertEqual(response.status_code, 200)
