from credentials import *
import generate_coordinates
import api_queries
import map_plotting
# The main file

# Credentials
# creds is imported so key will be api_key

# create coordinates from values in credentials
# args:
#   start latitude
#   start longitude
#   finish latitude
#   finish longitude
coordinates = generate_coordinates.Coordinates(sc[0], sc[1], fc[0], fc[1], distance)
coordinates.write_coordinates()


# Running the query against the api
query = api_queries.Query(coordinates.get_coordinates())  # init
query.get_requests()  # Get a list or url api calls to make
print(query.get_call_counts())  # Print a message about how many calls this will be
query.write_file(query.get_data())

map_plotting.create_searched_area_map()
map_plotting.create_results_map()

# Class to take the query data returned and write to json.

#TODOs
# next page data
# map drawing
# - create a kml file to make a map and print a link to the 'searched area' out in the terminal, better yet an image
# into ./app/data