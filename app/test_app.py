import unittest
from app.main import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Flask CI/CD app!", response.data)

if __name__ == "__main__":
    unittest.main()