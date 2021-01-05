# Imports
import json

import requests

import config
from scraping.models import Country, Account, Category


class Scraper(object):
    # Declare global variables
    BASE_URL = config.BASE_URL
    HEADERS = {
        "x-requested-with": "XMLHttpRequest",
        "cookie": config.COOKIE
    }
    params = {}
    country = Country()

    # Init init values
    def __init__(self, country_name, cookie):
        # Reading params for search
        self.read_params()
        self.country = Country.objects.filter(title=country_name).first()
        self.HEADERS["cookie"] = cookie

    # Functions
    def test_request(self):
        keywords = {
            "key1": 1,
            "key2": 2
        }

        payload = self.payload_maker(keywords)
        response = self.request_search(payload)
        self.read_response(response)

    def parse_all(self, max_followers_count=999999999):
        max_followers = max_followers_count
        accounts_left = 999999999

        while accounts_left > 1:
            keywords = {
                # filter followers count to
                self.params["search"]["followers"]["to"]: max_followers
            }

            payload = self.payload_maker(keywords)
            response = self.request_search(payload)
            result = self.read_response(response)

            if result["data"] == "no_data":
                print(f"Left accounts count: {accounts_left}")
                print(f"Next max followers count: {max_followers}")

                return max_followers

            cur_max_followers = result["data"]["max_followers"]
            if cur_max_followers == max_followers:
                max_followers = max_followers - 1
            else:
                max_followers = cur_max_followers
            accounts_left = result["data"]["accounts_left"]

    def payload_maker(self, keywords):
        # Payload with default(initial) values
        payload = {
            # type 0 is country
            self.params["search"]["influencer"]["location"]["type"]: 0,
            # 1522867 id of Kazakhstan
            self.params["search"]["influencer"]["location"]["id"]: self.country.hype_id,
            # Sort by followers count (desc - high to low)
            self.params["search"]["sort"]["followers"]: "desc"
        }

        return {**payload, **keywords}

    def request_search(self, payload):
        # Send requests with header and payload
        request = requests.get(self.BASE_URL, headers=self.HEADERS, params=payload)
        response = request.json()

        # Writing response to file
        with open('test_json.json', 'w') as outfile:
            json.dump(response, outfile)

        return response

    def read_response(self, response):
        # Testing response data
        accounts_list = response["data"]

        if len(accounts_list) < 1:
            print("NO DATA NO DATA NO DATA")

            return {
                "data": "no_data"
            }

        max_followers_count = accounts_list[-1][3]
        accounts_count = response["total"]

        print("Left accounts count: " + str(accounts_count) + "\n")
        print("Next max followers count: " + str(max_followers_count) + "\n")

        for account_json in accounts_list:
            # Check if account exist continue
            account = Account.objects.filter(username=account_json[2]["username"]).first()
            if account:
                continue

            # Else create account
            account = Account()
            account.name = account_json[2]["name"]
            account.username = account_json[2]["username"]
            account.is_verified = account_json[2]["is_verified"]
            account.followers = account_json[3]
            account.quality_followers = account_json[4]
            account.engagement_rate = account_json[5]
            account.account_quality_score = account_json[6]["title"]
            account.country = self.country

            # Save account
            account.save()

            # Set categories
            categories = account_json[7]
            categories = [Category.objects.filter(title=category).first().hype_id for category in categories]
            account.categories.set(categories)

            print(f"Creating account: {account.username}")
            print(f"Followers count: {account.followers}")
            print("\n")

        return {
            "data": {
                "max_followers": max_followers_count,
                "accounts_left": accounts_count
            }
        }

    def read_params(self):
        with open('data/params.json') as params_json_file:
            self.params = json.load(params_json_file)
