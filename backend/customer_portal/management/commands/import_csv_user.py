import csv
import os
from django.core.management.base import BaseCommand, CommandError
from customer_portal.models import Users
import pandas as pd


class Command(BaseCommand):
    help = "Import CSV file into user model"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        if not os.path.exists(csv_file_path):
            raise CommandError(f"The file {csv_file_path} does not exist")

        df = pd.read_csv(csv_file_path, delimiter = ";")

        for index, row in df.iterrows():
            user = Users(
                userID=row['userID'],
                userLastName=row['userLastName'],
                userFirstName=row['userFirstName'],
                userEmail=row['userEmail'],
                userPhone=row['userPhone'],
                companyID=row['companyID'],
            )
            created = user.save()
            self.stdout.write("created")
