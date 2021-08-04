from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPI(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_new_user_success(self):
        """Test create user is success"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha1234'
        }

        res = self.client.post(CREATE_USER_URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(data['password']))

    def test_creating_exist_user_fails(self):
        """Test create user that is exist fails"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha1234'
        }

        create_user(**data)

        res = self.client.post(CREATE_USER_URL, data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_not_create_user_with_short_password(self):
        """Test can not create user with password shorten than 8"""

        data = {
            'name': 'Moha',
            'email': 'moha@django.com',
            'password': 'moha123'
        }

        res = self.client.post(CREATE_USER_URL, data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
