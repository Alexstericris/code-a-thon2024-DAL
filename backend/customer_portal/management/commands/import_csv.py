import csv
import os
from django.core.management.base import BaseCommand, CommandError
from customer_portal.models import Company
import pandas as pd


class Command(BaseCommand):
    help = "Import CSV file into Company model"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        if not os.path.exists(csv_file_path):
            raise CommandError(f"The file {csv_file_path} does not exist")

        df = pd.read_csv(csv_file_path)

        for index, row in df.iterrows():
            company = Company(
                companyID=row['companyID'],
                companyName=row['companyName'],
                companyStreet=row['companyStreet'],
                companyPLZ=row['companyPLZ'],
                companyBranche=row['companyBranche'],
                companyEmail=row['companyEmail'],
                companyTradingID=row['companyTradingID'],
                companyCourt=row['companyCourt'],
            )
            created = company.save()
            self.stdout.write("created")
