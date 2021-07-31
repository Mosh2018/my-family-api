from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
import time


class Command(BaseCommand):
    """Django command to pause exceution until database connection is available"""
    def handle(self, *args, **options):
        self.stdout.write('Waiting database connection....')
        conn = None
        while not conn:
            try:
                conn = connections['default']

            except OperationalError:
                self.stdout.write(self.style.WARNING('connection unavailable waiting for connection :('))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available :) '))
