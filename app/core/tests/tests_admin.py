from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminSiteTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='admin@django.fi', password='moha0000')
        self.user = get_user_model().objects.create_user(
            email='user@django.fi',
            password='moha0000',
            name='Moha full name')

        self.client.force_login(self.admin_user)

    def test_user_listing(self):
        """get list of users"""

        res = self.client.get(reverse('admin:core_user_changelist'))

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
