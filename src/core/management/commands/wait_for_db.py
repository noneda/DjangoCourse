"""
Django Command to Wait for the database to be available
"""

import time

from psycopg2 import OperationalError as PsyOpeErr

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError as OpeErr


class Command(BaseCommand):
    """
    Django Command to Wait for the database
    """

    def handle(self, *args, **options):
        """Entrypoint for commands"""
        self.stdout.write("Waiting for Database...")

        db_use = False
        while db_use is False:
            try:
                self.check(databases=["default"])
                db_use = True
            except (PsyOpeErr, OpeErr):
                self.stdout.write("Database unavailable, waiting a 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("DATABASE available!!"))
