'''Questions tests'''

from .basetests import BaseTest

class TestViews(BaseTest):
    """Tests for questions"""


    def test_post_question(self):
        """Test post question endpoint"""
        response = self.post_question()
        self.assertEqual(response.status_code, 201)

    def test_empty_strings(self):
        """Test empty question field"""
        response = self.post_empty_question_field()
        self.assertEqual(response.status_code, 400)

    def test_get_all_questions(self):
        """Test empty question field"""
        response = self.get_all_questions()
        self.assertEqual(response.status_code, 200)

    def test_get_one_question(self):
        """Test empty question field"""
        response = self.get_one_question()
        self.assertEqual(response.status_code, 200)

    def test_one_question_doesnt_exist(self):
        """Test empty question field"""
        response = self.get_one_question_doesnt_exist()
        self.assertEqual(response.status_code, 404)
