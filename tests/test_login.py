import json

from tests.basecase import BaseCase

class TestUserLogin(BaseCase):

    def test_successful_login(self):
        # Given
        email = "testcase2@gmail.com"
        password = "mycoolpassword"
        payload = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        # When
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['access_token']))
        self.assertEqual(200, response.status_code)