'''Tests for users'''
from .basetests import BaseTest

class TestUsers(BaseTest):
    """Test user registration and login"""
    def test_user_login(self):
        """Test user login endpoint"""
        response = self.login()
        self.assertEqual(response.status_code, 200)

    def test_missing_first_name(self):
        """Test missing field"""
        response = self.missing_first_name()
        self.assertEqual(response.status_code, 401)

    def test_missing_last_name(self):
        """Test missing field"""
        response = self.missing_last_name()
        self.assertEqual(response.status_code, 401)

    def test_user_phonenumber(self):
        """Test missing field"""
        response = self.missing_phone_number()
        self.assertEqual(response.status_code, 401)

    def test_missing_email(self):
        """Test missing field"""
        response = self.missing_email()
        self.assertEqual(response.status_code, 401)

    def test_missing_image(self):
        """Test missing field"""
        response = self.missing_image()
        self.assertEqual(response.status_code, 401)

    def test_missing_password(self):
        """Test missing field"""
        response = self.missing_password()
        self.assertEqual(response.status_code, 401)

    def test_missing_confirm_password(self):
        """Test missing field"""
        response = self.missing_confirm_password()
        self.assertEqual(response.status_code, 401)

    def test_unequal_passwords(self):
        """Test unmatched passwords"""
        response = self.unmatched_passwords()
        self.assertEqual(response.status_code, 401)

    def test_invalid_email_format(self):
        """Test invalid email"""
        response = self.invalid_email()
        self.assertEqual(response.status_code, 400)
