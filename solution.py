import itertools
from fetch import *
from plot import draw_map

distances = []

def distance(x,y):
  return distances[x][y]

def route_length(route):
  """Distance between first and last and consecutive elements of a list."""
  return sum(distance(route[i],route[i - 1]) for i in range(len(route)))

def all_routes(seq):
  """Return all permutations of a list, each starting with the first item"""
  return [[seq[0]] + list(rest) for rest in itertools.permutations(seq[1:])]

def partition(collection):
  """Returns the set of all partitions for a given set
    e.g for [1,2], it returns [[1],[2]] and [[1,2]]"""
  if len(collection) == 1:
    yield [collection]
    return
  first = collection[0]
  for smaller in partition(collection[1:]):
    for n, subset in enumerate(smaller):
      yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
    yield [[first]] + smaller

def shortest_route(routes):
  """Given a list of routes returns the minimum based on route length"""
  return min(routes, key=route_length)

def all_short_routes_with_partitions(ids, partitions=1):
  """Our partitions represent number of vehicles. This function yields
     an optimal path for each vehicle given the destinations assigned to it"""
  for p in partition(ids[1:]):
    if len(p) == partitions:
      yield [shortest_route(all_routes([ids[0]] + q)) for q in p]

def shortest_route_with_partitions(loc_ids, partitions=1):
  """This function receives all k-subsets of a route and returns the subset
    with minimum distance cost. Note the total time is always equal to
    the max time taken by any single vehicle"""
  return min(all_short_routes_with_partitions(loc_ids, partitions),
             key=lambda x: max(route_length(x[i]) for i in range(partitions)))

if __name__ == '__main__':
  search_query = "McDonalds near Lahore City"
  locations = get_locations(search_query)
  location_ids = [l['Id'] for l in locations]
  distances = get_distances(locations, search_query)
  t0 = time.clock()
  shortest_route = shortest_route_with_partitions(location_ids, 2)
  paths = get_paths(locations,shortest_route)

  draw_map(locations, [], "input.html")
  draw_map(locations, paths, 'output.html')

  print('Time elapsed: {0:.2f} seconds'.format(time.clock() - t0))

  print('Shortest route time: {0:.1f} minutes'.
        format(max(route_length(i) for i in shortest_route)))

  print('Shortest route is: {0}'.format(shortest_route))
