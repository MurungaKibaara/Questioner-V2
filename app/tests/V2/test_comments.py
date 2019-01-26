'''Questions tests'''

from .basetests import BaseTest

class TestViews(BaseTest):
    """Tests for questions"""

    def test_post_comments(self):
        """Test post question endpoint"""
        response = self.post_comments()
        self.assertEqual(response.status_code, 201)

    def test_empty_strings(self):
        """Test empty question field"""
        response = self.post_empty_comment_field()
        self.assertEqual(response.status_code, 400)

    def test_get_all_comments(self):
        """Test empty question field"""
        response = self.get_all_comments()
        self.assertEqual(response.status_code, 200)

    def test_get_one_comment(self):
        """Test empty question field"""
        response = self.get_one_comment()
        self.assertEqual(response.status_code, 200)

    def test_one_comment_doesnt_exist(self):
        """Test empty question field"""
        response = self.get_one_comment_doesnt_exist()
        self.assertEqual(response.status_code, 404)
