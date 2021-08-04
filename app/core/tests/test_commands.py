from unittest import TestCase
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError


class CommandTest(TestCase):
    def test_connection_for_dd(self):
        """Connection for database success"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_waiting_for_db_connection(self, times):
        """Waiting for database connectios 5 times"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
