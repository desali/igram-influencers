from django.core.management import BaseCommand

from scraping.scraper import Scraper


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Task running!")

        scraper = Scraper(country_name="Kazakhstan")
        scraper.parse_all(max_followers_count=113261)
