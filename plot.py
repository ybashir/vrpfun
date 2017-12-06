import csv
import polyline

from gmplot import GoogleMapPlotter
key = 'AIzaSyD8n-hyKVeAKHx6D4OrsYPxKEF8ultGAmE'


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

  def write_point(self, f, lat, lon, color, title):
    f.write('\t\tvar latlng = new google.maps.LatLng(%f, %f);\n' %
            (lat, lon))
    if title =='1':
      f.write('\t\tvar img = new google.maps.MarkerImage(\'https://image.ibb.co/cUXPSw/truck_catering.png\');\n')
    f.write('\t\tvar marker = new google.maps.Marker({\n')

    if title=='1':
      f.write('\t\ticon: img,\n')
    else:
      f.write('\t\tlabel: "%s",\n' % title)

    f.write('\t\tposition: latlng\n')
    f.write('\t\t});\n')
    f.write('\t\tmarker.setMap(map);\n')
    f.write('\n')


lat,lng = GoogleMapPlotterPlus.geocode("Lahore")
gmap = GoogleMapPlotterPlus(lat,lng,zoom=13,apikey=key)


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
  with open('locations.csv','r') as file:
    reader = csv.DictReader(file)
    draw_map(reader,None,'input.html')
