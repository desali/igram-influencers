# Imports
import time
import json
import requests

from models.Account import Account


class Scraper(object):

	# Declare global variables
	BASE_URL = "https://app.hypeauditor.com/discovery/ajax/?search"
	HEADERS = {
		"x-requested-with": "XMLHttpRequest",
		"cookie": "__cfduid=da296a87e40222e1b4f6702d8e0583e9c1583663901; landing-abtest-feb20=1; last_404=%2Fsm%2F28100b9317e223285ed1ed454859381d29568d8a90bf722c8a2e3eb42ca86aff.map%2F; _ga=GA1.2.684726611.1583674704; _gid=GA1.2.407772502.1583674704; hubspotutk=51af77537e424afa7cdb0f2ea1d64e22; __hssrc=1; G_ENABLED_IDPS=google; intercom-id-tznjiue2=042f1e58-7f3b-4f19-b672-fd4adde88458; kyb-account=741270; kyb-hash=%242y%2404%24OLKTjDNryJt9PdwSzy8jFOI7Kkn3HcF4lzn3w1vIV8CMgMK3VH4VO; _dc_gtm_UA-97700016-3=1; __hstc=148432680.51af77537e424afa7cdb0f2ea1d64e22.1583674704614.1583674704614.1583678554723.2; kyb-m=tatehamfax%40gmail.com; __stripe_mid=440da607-ab86-48b2-a1c1-0ffdb38fb6fe; __stripe_sid=277ed577-6166-450e-8a8b-ad93b48e40f6; _ga=GA1.3.684726611.1583674704; _gid=GA1.3.407772502.1583674704; __hssc=148432680.2.1583678554723; intercom-session-tznjiue2=ZnpEUnhkWVArcll4eXNsSHRRNjI1c2piSXlJcWF6djJIMGI1YzZvbUlnMnlTTFJTYjZDbXcxdFF4S01hTkNGaS0tRGlVWVVuK2xsVzA4cVRuWlZvZVNVZz09--931d1afc86962bc2889dcf025214ecb6650aa3a9; amplitude_id_fdb01fff6a804dba1f464a3e9942cfb6hypeauditor.com=eyJkZXZpY2VJZCI6IjFkZDM2ODFhLTBmNmYtNDczZC1hNDQ4LTdlNzIzODFlZmM0NVIiLCJ1c2VySWQiOiI3NDEyNzAiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1ODM2Nzg0NTE0ODgsImxhc3RFdmVudFRpbWUiOjE1ODM2Nzg1ODc3ODIsImV2ZW50SWQiOjEzLCJpZGVudGlmeUlkIjo3LCJzZXF1ZW5jZU51bWJlciI6MjB9"
	}
	params = {}

	# Init init values
	"""Scraper main class"""
	def __init__(self):
		# Reading params for search
		self.read_params()


	# Functions
	def test_request(self):

		keywords = [
			"key:1",
			"value:1"
		]

		payload = self.payload_maker(keywords)
		response = self.request_search(payload)
		self.read_response(response)


	def payload_maker(keywords):
		
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
			if(key.split(":")[0] == "key"):
				print("hey")
			elif(key == "value"):
				print("value")

		return payload

	def request_search(payload):
		# Send requests with header and payload
		request = requests.get(self.BASE_URL, headers=self.HEADERS, params=payload)
		response = request.json()

		# Writing response to file
		with open('test_json.txt', 'w') as outfile:
			json.dump(response, outfile)

		return response

	def read_response(response):
		# Testing response data
		accounts_count = response["total"]
		accounts_list = response["data"]

		print("Total accounts count: " + str(accounts_count) + "\n")

		for account_json in accounts_list:
			name = account_json[2]["name"]
			username = account_json[2]["username"]
			is_verified = account_json[2]["is_verified"]
			followers = account_json[3]
			quality_followers = account_json[4]
			engagement_rate = account_json[5]
			account_quality_score = account_json[6]["title"]
			categories = account_json[7]

			 

			print(account)
			print("\n")


		max_followers_count = accounts_list[0][3]


	def read_params(self):
		with open('data/params.json') as params_json_file:
			self.params = json.load(params_json_file)
