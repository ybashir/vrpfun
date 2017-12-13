# A pythonic but brute-force solution for the Vehicle Routing Problem (VRP)

VRP is a generalized version of the Traveling Salesperson Problem (TSP): Given a depot, a set of delivery locations and the number of vehicles starting from the depot, we need to minimize the time (or travel distance) required to visit all locations.

This repo is a pythonic implementation of the brute-force solution to the VRP. VRP is an NP-Hard problem so the brute force obviously becomes very prohibitive very quickly as the number of destinations is increased or the number of vehicles is reduced. 

However, the idea here is just to show how a few lines of python code can be used to solve hard problems.

The code expects two input files, one with locations and their geo-coordinates and the other with distances between locations. There are some simplistic assumptions:

1. Each delivery location needs to be visited just once
2. Vehicles come back to the depot
3. The first location in the list of locations is the depot
4. Distance from X to Y is the same as the distance from Y to X

Here is a sample plot of the starting input locations resulting from search query ```McDonalds near Lahore``` with the truck icon showing the depot:


![alt text](https://i.imgur.com/82QgV4X.jpg)

Here is the output and plot created after the algorithm has been run with 3 vehicles as input:
```
Solution time: 69.06 seconds (with pypy which is roughly 6x faster than PythonC)
Shortest route time: 47.7 minutes
Shortest route is: [[0, 5, 8], [0, 4, 11, 2, 10, 6], [0, 1, 9, 12, 7]]
```

![alt text](https://i.imgur.com/HnqfAFS.jpg)

To try this out, clone the repo and install dependencies (ideally in a virtualenv):

```pip install -r requirements.txt```

Update the settings file to include your own settings, especially these two:

```
GOOGLE_MAPS_KEY = 'Add your own google maps key here'
LIMIT_LOCATIONS = 12
```
If you run the algorithm for more than 12 locations, be prepared to wait a very long time for the results :)

Finally, supply command line arguments and run the code like this:

```python solution.py <search_query> <number_of_vehicles>```

e.g.

```python solution.py "Sample" 3```

After the first run, your input files will be automatically created and the results dont need to be fetched again. You can add a depot location at the top of the created input file for locations.
