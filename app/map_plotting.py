from gmplot import gmplot
from credentials import *
import json

def create_searched_area_map():
    with open('data/coordinates.json', 'r') as f:
        data = json.load(f)

    # Place map
    gmap = gmplot.GoogleMapPlotter(sc[0], sc[1], 10)
    # Scatter points

    longs = []
    lats = []
    for d in data:
        lats.append(d['latitude'])
        longs.append(d['longitude'])
    gmap.scatter(lats, longs, 'red')

    # Marker
    hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689

    # Draw
    gmap.draw("maps/area_searched.html")

def create_results_map():
    with open('data/list_of_healers.json', 'r') as f:
        data = json.load(f)


    # Place map
    gmap = gmplot.GoogleMapPlotter(sc[0], sc[1], 10)
    # Scatter points

    _longs = []
    _lats = []
    counter = 1
    for d in data:
        counter += 1
        _lats.append(d['lat'])
        _longs.append(d['long'])
    gmap.scatter(_lats, _longs, 'red')
    print(counter)
    # Marker
    # Draw
    gmap.draw("maps/results.html")

# with open('data/list_of_healers.json', 'r') as f:
#     data = json.load(f)
#
#     _longs = []
#     _lats = []
#     counter = 1
#     for d in data:
#         counter += 1
#         _lats.append(d['lat'])
#         _longs.append(d['long'])
#         print(d['name'])
#
#     print(counter)
#     # Marker
#     # Draw
