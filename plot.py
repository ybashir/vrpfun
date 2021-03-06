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

class GoogleMapPlotterPlus(GoogleMapPlotter):
  """
  Slight variation on https://github.com/vgm64/gmplot
  changes the image marker for the zeroeth location and adds labels to the others
  """

  def write_point(self, f, lat, lon, color, title):
    f.write('\t\tvar latlng = new google.maps.LatLng(%f, %f);\n' %
            (lat, lon))
    f.write('\t\tvar img = new google.maps.MarkerImage(\'https://image.ibb.co/cUXPSw/truck_catering.png\');\n')
    f.write('\t\tvar marker = new google.maps.Marker({\n')
    if title=='0' or title == 0:
      f.write('\t\ticon: img,\n')
    else:
      f.write('\t\tlabel: "%s",\n' % title)
    f.write('\t\tposition: latlng\n')
    f.write('\t\t});\n')
    f.write('\t\tmarker.setMap(map);\n')
    f.write('\n')


lat,lng = GoogleMapPlotterPlus.geocode("Lahore")
if lat and lng:
  gmap = GoogleMapPlotterPlus(lat,lng,zoom=13,apikey=key)
else:
  print("Google maps call failed. Try again")

def draw_locations(locations):
  global gmap
  for loc in locations:
    gmap.marker(float(loc['Lat']),float(loc['Lon']),"olivedrab",title=loc['Id'])

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
