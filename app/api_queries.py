# The google places api query including next page data
import urllib, json, os
import urllib.request
from credentials import *
import generate_coordinates
import time

# given the coordinats list we have,
# loop over and run the query
class Query:
	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.requests = []
		# list for the results
		self.results = []

	#given the list, create an array of api urls to reques
	def get_requests(self):
		for coordinate in self.coordinates:
			my_url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
			          'location=%s,%s'
			          '&radius=%s'
			          '&keyword=%s'
			          '&key=%s') % (coordinate[0], coordinate[1], radius, keyword, api_key)
			# grabbing the JSON result
			self.requests.append(my_url)

	def get_call_counts(self):
		return 'This will ammount to {} individual api calls.'.format(len(self.requests))


	def get_data(self):
		# test with 1 request first
		counter = 0
		# take slice 133 to 143 for next page tokens
		for a_url in self.requests:
			with urllib.request.urlopen(a_url) as url:
				response = url.read()
				json_data = json.loads(response)

				for result in json_data["results"]:
					location = result['geometry']['location']
					a_healer = {
						'name': result["name"],
						'vicinity': result['vicinity'],
						'lat': location['lat'],
						'long': location['lng'],
					}
					self.results.append(a_healer)

				if 'next_page_token' in json_data:
					# start looping and writing
					print(' ============ next page found ===========')
			counter += 1
			print('total API calls: {}'.format(counter))

		return self.results

	def write_file(self,data):
		with open('data/list_of_healers.json', 'w') as f:
			json.dump(data, f)

