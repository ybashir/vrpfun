import googlemaps

GOOGLE_MAPS_KEY = 'Add your own google maps key here or in a local_settings file'

MAX_LOCATIONS = 100
SEARCH_RADIUS = 25000

try:
  import local_settings
  GOOGLE_MAPS_KEY = local_settings.GOOGLE_MAPS_KEY
except:
  pass

gmaps_client = googlemaps.Client(key=GOOGLE_MAPS_KEY)

