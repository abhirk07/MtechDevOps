import unittest
from app import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from Flask", response.data)

    def test_status(self):
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"OK", response.data)

if __name__ == '__main__':
    unittest.main()
