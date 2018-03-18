import urllib, json, os
import urllib.request
import time

my_results = []


def next_page_data(page_token):
	#build a new next page query
	#eg https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken=PAGE_TOKEN&key=YOUR_API_KEY
# better https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.509865,-0.118092&radius=10000&keyword=spiritual&key=AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k
	key = 'AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k'
	location = '51.509865' + "," + '-0.118092'
	radius = '1000'
	keyword = 'spiritual'
	my_url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
	          'location=%s'
	          '&radius=%s'
	          '&keyword=%s'
              '&key=%s'	
	          '&pagetoken=%s') % (location, radius, keyword, key, page_token)
	# execute the query and populate page 2
	print(my_url)
	with urllib.request.urlopen(my_url) as url:
		response = url.read()
		json_data = json.loads(response)

		for result in json_data["results"]:
			a_healer = {'name': result["name"]}
			my_results.append(a_healer)

		if 'next_page_token' in json_data:
			# start looping and writing
			print('next page found')
			time.sleep(10)
			next_page_data(json_data["next_page_token"])



def places():
	# making the url
	key = 'AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k'
	location = '51.509865' + "," + '-0.118092'
	radius = '50000'
	keyword = 'spiritual'
	my_url = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
	          'location=%s'
	          '&radius=%s'
	          '&keyword=%s'
	          '&key=%s') % (location, radius, keyword, key)
	# grabbing the JSON result
	with urllib.request.urlopen(my_url) as url:
		response = url.read()
		json_data = json.loads(response)

		for result in json_data["results"]:
			a_healer = {'name': result["name"]}
			my_results.append(a_healer)

		if 'next_page_token' in json_data:
			# start looping and writing
			print('next page found')
			time.sleep(10)
			next_page_data(json_data["next_page_token"])




places()


def write_file(data):
	with open('list_of_healers.json', 'w') as f:
		json.dump(data, f)


write_file(my_results)


# make query1
# next page query
# get data from above
# dump into json





