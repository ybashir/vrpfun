import time
import csv
from settings import *
from utils import *

def get_locations(search_query):
  locations = []
  filename = slugify(search_query) + '_locations.csv'
  try:
    with open(filename,'r') as f:
      for row in csv.DictReader(f):
        row['Id'] = int(row['Id'])
        row['Lat'] = float(row['Lat'])
        row['Lon'] = float(row['Lon'])
        locations.append(row)
  except IOError:
    locations = fetch_locations(search_query,filename)
  return locations[:MAX_LOCATIONS]

def get_distances(locations, search_query, track='duration'):
  filename = slugify(search_query) + '_distances.csv'
  try:
    with open(filename,'r') as f:
      distances = [[0] * MAX_LOCATIONS for _ in range(MAX_LOCATIONS)]
      for row in csv.DictReader(f):
        x, y = int(row['start']), int(row['end'])
        distances[x][y] = distances[y][x] = float(row[track])
      return distances
  except IOError:
    return fetch_distances(locations, filename, track)

def get_paths(locations, route):
  paths = []
  for path in route:
    d = {l['Id']: l for l in locations}
    directions = gmaps_client.directions(
      origin=stringify_latlong(d[path[0]]),
      destination=stringify_latlong(d[path[-1]]),
      waypoints=[stringify_latlong(d[path[i]]) for i in range(1, len(path) - 1)])
    paths.append(directions[0]['overview_polyline']['points'])
  return paths

def fetch_locations(search_query, filename='locations.csv'):
  locations = []
  page_token = None
  i = 0
  with open(filename,'w', encoding='utf-8') as f:
    fieldnames = ['Id', 'Address', 'Lat', 'Lon']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    while True:
      results = gmaps_client.places(search_query,
                                    page_token=page_token)
      for r in results['results']:
        row = {
          'Id': i,
          'Address': r['formatted_address'],
          'Lat': float(r['geometry']['location']['lat']),
          'Lon': float(r['geometry']['location']['lng'])
        }
        locations.append(row)
        writer.writerow(row)
        i += 1
      if 'next_page_token' not in results:
        break
      page_token = results['next_page_token']
      time.sleep(2)
  return locations

def fetch_distances(locations, filename='distances.csv', track='duration'):
  distances = [[0] * MAX_LOCATIONS for _ in range(MAX_LOCATIONS)]
  with open(filename,'w', encoding='utf-8') as f:
    fieldnames = ['start', 'end', 'distance', 'duration']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for i, l1 in enumerate(locations):
      for j, l2 in enumerate(locations):
        if j <= i: continue
        x = int(l1['Id'])
        y = int(l2['Id'])
        time.sleep(1)
        dist = gmaps_client.distance_matrix(origins=stringify_latlong(l1),
                                            destinations=stringify_latlong(l2))
        distance = dist['rows'][0]['elements'][0]['distance']['value'] / 1000
        duration = dist['rows'][0]['elements'][0]['duration']['value'] / 60
        distances[x][y] = distances[y][x] = {'distance': distance,
                                             'duration': duration}[track]
        row = {
          'start': x,
          'end': y,
          'distance': '{:.2f}'.format(distance),
          'duration': '{:.2f}'.format(duration)
        }
        print(row)
        writer.writerow(row)
  
  return distances
