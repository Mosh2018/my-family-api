from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_custom_user_success(self):
        """Create custom test and will success"""
        email = 'django@email.com'
        password = 'mosh1234'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """email for new user is normalized"""

        email = 'DjanGo@email.com'
        password = 'mosh1234'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_user_with_invalid_email(self):
        """User must has en email adress"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345678')

    def test_create_super_user(self):
        """Create super user"""

        email = 'DjanGo@email.com'
        password = 'mosh1234'
        user = get_user_model().objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
