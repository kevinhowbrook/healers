import urllib, json, os
import urllib.request
import time

def next_page_data(page_token):
	#build a new next page query
	#eg https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken=PAGE_TOKEN&key=YOUR_API_KEY

	key = 'AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k'
	key = 'AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k'
	location = '51.509865' + "," + '-0.118092'
	radius = '1000'
	types = 'spiritual+healers'
	my_url = ('https://maps.googleapis.com/maps/api/place/textsearch/json?query='
	          '%s'
	          '&location=%s'
	          '&radius=%s'
	          '&sensor=false&key=%s'
	          '&pagetoken=%s') % (types, location, radius, key, page_token)
	print(my_url)
	# execute the query and populate page 2
	with urllib.request.urlopen(my_url) as url:
		response = url.read()
		json_data = json.loads(response)

	with open('data/data_all.json', 'a') as outfile:
		json.dump(json_data, outfile)

	if json_data["next_page_token"]:
		# start looping and writing
		time.sleep(10)
		next_page_data(json_data["next_page_token"])

def google_places():
	'''Basically this just gives us the first page of results and our first page token'''
	# making the url
	key = 'AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k'
	location = '51.509865' + "," + '-0.118092'
	radius = '1000'
	types = 'spiritual+healers'
	my_url = ('https://maps.googleapis.com/maps/api/place/textsearch/json?query='
	       '%s'
	       '&location=%s'
	       '&radius=%s'
	       '&sensor=false&key=%s') % (types, location, radius, key)
	# grabbing the JSON result
	with urllib.request.urlopen(my_url) as url:
		response = url.read()
		json_data = json.loads(response)

	if json_data["next_page_token"]:
		# start looping and writing
		time.sleep(10)
		next_page_data(json_data["next_page_token"])

	with open('data/data_all.json', 'a') as outfile:
		json.dump(json_data, outfile)

	# if there is a next page cache token run another function

google_places()



# next page token eg = https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken=CrQCJAEAAMEv_-3FEBKB6GFLASwA3Hut-YJ4sNVKG5dqAbPFfIbe9kmAe8O-Zj6-0m_kaHyICxQ0vyX-IZ19kViT-3jryhbSJKRfqEQAv0M9eyFSLzVBjGDw-Q5bIeP4yDVi3yHj6LEoOwZV2fkvYNyqy0IigFxSf5K5G4PbpC16uMDOQmuKRQ1NljsyE8xufn8zaKm7eq1tqosMcvoluT_hrErVGlzVMvky9_LPc0Y_1rAI5vEc_8Z6TSa-bsu1KMaT-tK-lgK-1vuV4xduyP3X8bci-JJPXhDN8ZKOUI1k-l817lADrZ-qE1jLgd_sos4HPMd7IEUva1Jrnfg737VbvpiQEn5_oYRRFD5l0ZTl4_7hjPoyrwyjo0RXeHioZ05Yi0-FCDWNPq-Io9W1RuQjeMR5wpYSECEsiD4hlRo2USKSTZpeJuwaFCxl5MI08EkbBhpOrMBT-CpZW8Qu&key=AIzaSyAg1JppPI2AZRyskfSsrRVShdTDoZ8QW7k

# function to make query which runs add to json, then

# function to basically add data from a query to data.json

# def populate_data_from_request(query):


def json_read():
	data = json.load(open('data/data_all.json'))

	my_results = []
	for result in data["results"]:
		a_healer = {'name': result["name"]}
		my_results.append(a_healer)


	with open('list_of_healers.json', 'w') as f:
		json.dump(my_results, f)



json_read()



