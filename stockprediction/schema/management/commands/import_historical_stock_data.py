from __future__ import unicode_literals
import csv
from django.core.management.base import BaseCommand
from django.utils.encoding import force_text
from ...models import HistoricalStockData, Stocks

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
    help = (
        "Imports movies from a local CSV file. "
        "Expects title, URL, and release year."
    )

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            "file_path",
            nargs=1
        )

    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)
        file_path = options["file_path"][0]

        if verbosity >= NORMAL:
            self.stdout.write("=== Movies imported ===")

        with open(file_path) as f:
            reader = csv.reader(f)
            s1 = Stocks(stock_id="MST", company="MICROSOFT", ticker ="MSFT",
            industry="IT", sector="Software")
            s1.save()
            for rownum, (date,op,high,low,close,volume) in \
            enumerate(reader):
                """
                if rownum == 0:
                    # let's skip the column captions
                    continue
                """
                data, created = HistoricalStockData.objects.get_or_create(
                    stock_id=s1,
                    date=force_text(date),
                    open=force_text(op),
                    high=force_text(high),
                    low=force_text(low),
                    close=force_text(close),
                    volume=force_text(volume)
                )
