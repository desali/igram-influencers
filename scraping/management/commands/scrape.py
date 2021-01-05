from django.core.management import BaseCommand

from scraping.scraper import Scraper

import config


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Task running!")

        max_followers_count = 22064

        for cookie in config.COOKIES:
            print(cookie)

            scraper = Scraper(country_name="Russia", cookie=cookie)
            max_followers_count = scraper.parse_all(max_followers_count=max_followers_count)
