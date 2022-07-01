import csv
import polyline
import sys

import settings
from gmplot import GoogleMapPlotter
key = settings.GOOGLE_MAPS_KEY

colors = [
  'darkblue',
    'darkcyan',
    'darkgoldenrod',
    'darkgray',
    'darkgreen',
    'darkkhaki',
    'darkmagenta',
    'darkolivegreen',
    'darkorange',
    'darkorchid',
    'darksalmon',
    'darkseagreen'
]
lat,lng = GoogleMapPlotter.geocode(settings.DEFAULT_MAP_SETTING,apikey=key)
if lat and lng:
  gmap = GoogleMapPlotter(lat,lng,zoom=13,apikey=key)
else:
  print("Google maps call failed. Try again")

def draw_locations(locations):
  global gmap
  for i,loc in enumerate(locations):
    if i==0:
      gmap.marker(float(loc['Lat']),float(loc['Lon']),color='yellow',label=loc['Id'],title=loc['Address'],info_window="Depot")
    else:
      gmap.marker(float(loc['Lat']),float(loc['Lon']),color="salmon",label=loc['Id'],title=loc['Address'])

def draw_map(locations,paths,file):
  global gmap
  draw_locations(locations)
  for i,path in enumerate(paths):
    x,y = zip(*polyline.decode(path))
    gmap.plot(x,y,colors[i%10], edge_width=4)
  gmap.draw(file)

if __name__ == '__main__':
  filename = sys.argv[1]
  with open(filename,'r') as file:
    reader = csv.DictReader(file)
    draw_map(reader,[],'input.html')
