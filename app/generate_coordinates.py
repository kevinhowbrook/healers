# Class for generating a list of latitude and longitudes
# as a list []
import credentials
from math import pi, cos
import json

class Coordinates:
	def __init__(self, start_latitude, start_longitude, end_latitude, end_longitude, distance):
		self.start_latitude = start_latitude
		self.start_longitude = start_longitude
		self.end_latitude = end_latitude
		self.end_longitude = end_longitude
		# holder for new points
		self.coordinates = []
		self.lats = [start_latitude]
		self.longs = [start_longitude]
		self.r_earth = 6370
		self.distance = distance

		# populate the coordinates using below methods
		self.list_of_lats()
		self.list_of_longs()
		self.points_for_json = []

	def ll(self):
		print(self.lats, self.longs)

	# Creates a list of latitude values from start to finish with given distance
	def list_of_lats(self):
		while self.lats[-1] < self.end_latitude:
			new_latitude = self.lats[-1] + (self.distance / self.r_earth) * (180 / pi)
			if new_latitude > self.end_latitude:
				return
			self.lats.append(new_latitude)
			self.list_of_lats()

	# function to increase longitude values based on latitudes given
	def increase_long(self, _start_long, _input_lat):
		calc = _start_long + (self.distance / self.r_earth) * (180 / pi) / cos(_input_lat * pi / 180)
		return calc

	# given the latitudes we have, create a list of longitudes
	# and merge them to a new list
	def list_of_longs(self):
		for lat in self.lats:
			# create a number of longs relative to the lat we are given and the lenght of lats
			# create a list of longs relative to this lattitude
			new_longitude = self.start_longitude
			new_longs = []
			new_longs.append(self.start_longitude)

			while new_longs[-1] < self.end_longitude:
				new_longitude = self.increase_long(new_longs[-1], lat)
				new_longs.append(new_longitude)

			for l in new_longs:
				if l < self.end_longitude:
					self.coordinates.append([lat, l])

				# work out how many times we need to increase long to get to the end long

	def get_coordinates(self):
		return self.coordinates

	def write_coordinates(self):
		for point in self.coordinates:
			point = {'latitude': point[0], 'longitude': point[1]}
			self.points_for_json.append(point)

		with open('data/coordinates.json', 'w') as f:
			data = json.dump(self.points_for_json, f)

