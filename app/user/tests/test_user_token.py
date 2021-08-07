
from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APIClient

TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class TokenTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_token_created_successfully_with_valid_credentials(self):
        """create token for valid credentials"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha1234'
        }

        create_user(**data)

        login_data = {'email': data['email'], 'password': data['password']}

        res = self.client.post(TOKEN_URL, login_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)

    def test_create_token_invalid_credentials(self):
        """token will not generated with invalid credentials"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha1234'
        }
        create_user(**data)

        login_data = {'email': data['email'], 'password': 'moha1290'}
        res = self.client.post(TOKEN_URL, login_data)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_empty_password(self):
        """roken will not geberated with empty password"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha1234'
        }

        create_user(**data)

        login_data = {'email': data['email'], 'password': ''}
        res = self.client.post(TOKEN_URL, login_data)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Token will not generated with not exist user"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha1234'
        }

        create_user(**data)

        login_data = {'email': 'noONe@django.com', 'password': data['password']}
        res = self.client.post(TOKEN_URL, login_data)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authentication_is_required(self):
        """Test that user authentication is rquired"""

        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
