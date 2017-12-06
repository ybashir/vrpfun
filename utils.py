import re

def stringify_latlong(location):
  return '{0},{1}'.format(location['Lat'],
                          location['Lon'])

def slugify(sentence):
  return re.sub('\W','_',sentence.lower())


