import itertools,sys
from fetch import *
from plot import draw_map

distances = []

def distance(x, y):
  return distances[x][y]

def route_length(route):
  """Distance between first and last and consecutive elements of a list."""
  return sum(distance(route[i], route[i - 1]) for i, v in enumerate(route))

def all_routes(seq):
  """Return all permutations of a list, each starting with the first item"""
  return [[seq[0]] + list(rest) for rest in itertools.permutations(seq[1:])]

def all_partitions(collection):
  """Returns the set of all partitions for a given set
     e.g for [1,2], it returns [[1],[2]] and [[1,2]]
     https://stackoverflow.com/questions/19368375/set-partitions-in-python
  """
  if len(collection) == 1:
    yield [collection]
    return
  first = collection[0]
  for smaller in all_partitions(collection[1:]):
    for n, subset in enumerate(smaller):
      yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
    yield [[first]] + smaller

def shortest_route(routes):
  """Given a list of routes returns the minimum based on route length"""
  return min(routes, key=route_length)

def k_partitions_with_shortest_routes(ids, k=1):
  """Our partitions represent number of vehicles. This function yields
     an optimal path for each vehicle given the destinations assigned to it"""
  for p in filter(lambda x: len(x) == k,all_partitions(ids[1:])):
      yield [shortest_route(all_routes([ids[0]] + q)) for q in p]

def shortest_partition(loc_ids, partitions=1):
  """This function receives all k-subsets of a route and returns the subset
    with minimum distance cost. Note the total time is always equal to
    the max time taken by any single vehicle"""
  return min(k_partitions_with_shortest_routes(loc_ids, partitions),
             key=lambda x: max(route_length(x[i]) for i in range(partitions)))

if __name__ == '__main__':
  search_query = sys.argv[1]
  num_vehicles = int(sys.argv[2])
  limit_locations = int(sys.argv[3])
  locations = get_locations(search_query)
  location_ids = [l['Id'] for l in locations[:limit_locations]]
  distances = get_distances(locations, search_query)
  t0 = time.clock()
  shortest_route = shortest_partition(location_ids, num_vehicles)
  paths = get_paths(locations,shortest_route)

  draw_map(locations, [], "input.html")
  draw_map(locations, paths, 'output.html')

  with open('output.txt','a') as file:
    file.write('Solution time: {0:.2f} seconds\n'.format(time.clock() - t0))
    file.write('Shortest route time: {0:.1f} minutes\n'.
        format(max(route_length(i) for i in shortest_route)))
    file.write('Shortest route is: {0}\n'.format(shortest_route))
