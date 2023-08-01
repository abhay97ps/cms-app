"""
django command to wait for databse to be available
"""
import time

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for databse"""

    def handle(self, *args, **kwargs):
        """Entrypoint for command"""
        self.stdout.write('Waiting for databse...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database ready!'))
