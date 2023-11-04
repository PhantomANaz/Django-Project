from django.core.management.base import BaseCommand
from playground.models import SQLStockMarketTaskData
import json

class Command(BaseCommand):
    help = 'Load JSON data from a file into the database'

    def handle(self, *args, **options):
        with open('stock_market_data.json', 'r') as json_file:
            data = json.load(json_file)

        for item in data:
            SQLStockMarketTaskData.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully loaded JSON data from file into the database'))