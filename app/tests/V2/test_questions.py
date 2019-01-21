'''Questions tests'''

from .basetests import BaseTest

class TestViews(BaseTest):
    """Tests for questions"""


    def test_post_question(self):
        """Test post question endpoint"""
        self.registration()
        response = self.post_question()
        self.assertEqual(response.status_code, 201)

    def test_empty_strings(self):
        """Test empty question field"""
        self.create_meetup()
        response = self.post_empty_question_field()
        self.assertEqual(response.status_code, 401)
