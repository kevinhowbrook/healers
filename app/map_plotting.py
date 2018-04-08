from gmplot import gmplot
from PIL import Image, ImageDraw
from credentials import *
import json
import numpy as np
import matplotlib.pyplot as plt

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

def draw_map():
    img = Image.new('RGB', (1000, 1000), color='white')
    draw = ImageDraw.Draw(img, 'RGBA')

    img = Image.new("RGB", (400, 400), "white")
    draw = ImageDraw.Draw(img)

    coords = [(0.4, 0.4)]
    dotSize = 20

    for (x, y) in coords:
        draw.ellipse([x, y, x + dotSize - 1, y + dotSize - 1], fill="white", outline="pink")

    img.save('maps/out.png', 'PNG')


    # make a canvas of a relevant size from the sc and fc coordinates

    # for each value in coordinates, print a square on the canvas

def mp_test():
    # [x],[y]
    #plt.plot([51.46], [-0.05], 'ro')
    with open('data/list_of_healers.json', 'r') as f:
        data = json.load(f)

    unique_stuff = {each['name']: each for each in data}.values()

    _longs = []
    _lats = []
    counter = 1
    for d in unique_stuff:
        counter += 1
        _lats.append(d['lat'])
        _longs.append(d['long'])

    print(max(_longs))
    counter = 1

    for d in unique_stuff:
        plt.plot([float(d['long'])], [float(d['lat'])], 'ro')
        #plt.annotate('{} {}'.format(d['lat'], d['long']), xy=(d['lat'], d['long']), xytext=(d['lat'], d['long']))
        counter += 1

    plt.axis([min(_longs), max(_longs),min(_lats),max(_lats)])

    plt.show()