# Imports
import json

import requests

import config
from models.Account import Account


class Scraper(object):
    # Declare global variables
    BASE_URL = config.BASE_URL
    HEADERS = {
        "x-requested-with": "XMLHttpRequest",
        "cookie": config.COOKIE
    }
    params = {}

    # Init init values
    def __init__(self):
        # Reading params for search
        self.read_params()

    # Functions
    def test_request(self):
        keywords = {
            "key1": 1,
            "key2": 2
        }

        payload = self.payload_maker(keywords)
        response = self.request_search(payload)
        self.read_response(response)

    def payload_maker(self, keywords):
        # Payload with default(initial) values
        payload = {
            # type 0 is country
            self.params["search"]["influencer"]["location"]["type"]: 0,
            # 1522867 id of Kazakhstan
            self.params["search"]["influencer"]["location"]["id"]: 1522867,
            # Sort by followers count (desc - high to low)
            self.params["search"]["sort"]["followers"]: "desc"
        }

        for key in keywords:
            print(f"{key}: {keywords[key]}")

        return payload

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
        accounts_count = response["total"]
        accounts_list = response["data"]

        print("Total accounts count: " + str(accounts_count) + "\n")

        for account_json in accounts_list:
            account = Account()
            account.name = account_json[2]["name"]
            account.username = account_json[2]["username"]
            account.is_verified = account_json[2]["is_verified"]
            account.followers = account_json[3]
            account.quality_followers = account_json[4]
            account.engagement_rate = account_json[5]
            account.account_quality_score = account_json[6]["title"]
            account.categories = account_json[7]

            print(account)
            print("\n\n")

        max_followers_count = accounts_list[0][3]

    def read_params(self):
        with open('data/params.json') as params_json_file:
            self.params = json.load(params_json_file)
