import urllib, json, os, sys
import urllib.request
import time
from math import pi, cos

# Returns the formatted address from a query()
def return_formatted_address(query_string):
	with urllib.request.urlopen(query_string) as url:
		response = url.read()
		json_data = json.loads(response)

		for result in json_data["results"]:
			print(result["formatted_address"])

#return_formatted_address(query('51.509865','-0.118092'))



# Consider to change to tube map limits
# starting at bottom left of london ~ Woking
ll_start = [51.299711, -0.479279]
#[lat long]
# Finish at ro right ~ epping
ll_finish = [51.626010, 0.240326]

# holder for new points
points = []
longs = []
lats = []

lats.append(ll_start[0])
# increase long and lat by distance give
# return [long, lat]
counter = 0

# Creates a list of lattitude values from start to finish with given distance
def list_of_lats(start_lat, end_lat, dist):
	global counter
	counter += 1
	r_earth = 6378
	while lats[-1] < end_lat:
		new_latitude = lats[-1] + (10 / r_earth) * (180 / pi)
		if new_latitude > end_lat:
			return
		lats.append(new_latitude)
		list_of_lats(lats[-1], end_lat, 0.1)



list_of_lats(ll_start[0], ll_finish[0], 0.1)



# given the length of lats, work our how many times we need to populate new longs
#
#
def increase_long(start_long, dist, input_lat):
	r_earth = 6378
	calc = start_long + (dist / r_earth) * (180 / pi) / cos(input_lat * pi / 180)
	return calc
#
# given the lats, create a list of longs
def list_of_longs(start_long, end_long, dist, lats):
	r_earth = 6378

	lat_loop_counter = 0

	for lat in lats:
		#create a number of longs relative to the lat we are given and the lenght of lats
		# create a list of longs relative to this lattitude
		new_longitude = start_long
		new_longs = []
		new_longs.append(start_long)

		while new_longs[-1] < ll_finish[1]:
			new_longitude = increase_long(new_longs[-1], dist, lat)
			new_longs.append(new_longitude)
			lat_loop_counter += 1

		for l in new_longs:
			if l < ll_finish[1]:
				points.append([lat,l])

		# work out how many times we need to increase long to get to the end long

list_of_longs(ll_start[1], ll_finish[1], 0.1, lats)

# check we are not out of range
for ll in points:

	if ll[0] > ll_finish[0]:
		print('Lat out of range')
	if ll[1] > ll_finish[1]:
		print(ll[1], 'Long out of range')

# print the amount of point so we know how many api calls there will be

# def write_file(data):
# 	with open('testing.json', 'w') as f:
# 		json.dump(data, f)
#
# write_file(points)

# for each value in the lats list.
# calculate a new list of lats and longs
# new_longitude = long + (dist / r_earth) * (180 / pi) / cos(lat * pi / 180)
# so the new list will contain a multiple longs for each lat in the list
# ie
# [51.00, 00]
# [51.00, 01]
# [51.00, 02]
# [51.00, 03]
# [52.00, 00]
# [52.00, 01]
#
# etc
#
# def inc_long_and_lat(long,lat,dist):
# 	global counter
# 	counter += 1
# 	r_earth = 6378
# 	new_latitude = lat + (0.1 / r_earth) * (180 / pi)
# 	new_longitude = long + (dist / r_earth) * (180 / pi) / cos(lat * pi / 180)
# 	points.append([new_longitude, new_latitude])
# 	#print(new_longitude, new_latitude)
# 	print(counter)
# 	return [new_longitude, new_latitude]
#
#
# # Make a list of longs and lats to create an area
# def area():
#
# 	points.append(ll_start)
# 	next_ll = inc_long_and_lat(ll_start[0], ll_start[1], 0.1)
#
# 	while points[-1] < ll_finish:
#
# 		inc_long_and_lat(points[-1][0], points[-1][1], 0.1)
# 	# increase from start




# print(orig_long)
# print(new_longitude)
