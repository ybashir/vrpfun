# A pythonic but brute-force solution for the Vehicle Routing Problem (VRP)

VRP is a generalized version of the Traveling Salesperson Problem (TSP): Given a depot, a set of delivery locations and the number of vehicles starting from the depot, we need to minimize the time (or travel distance) required to visit all locations.

This repo is a pythonic implemetation of the brute-force solution to the VRP. VRP is an NP-Hard problem so the brute force obviously becomes very prohibitive very quickly as the number of destinations or the number of vehicles is increased. 

However, the idea here is just to show how a few lines of python code can be used to solve hard problems.

The code expects two input files, one with locations and their geo-coordinates and the other with distances between locations:

1. Vehicles have infinite capacity
2. Each delivery location needs to be visited just once
3. Vehicles come back to the depot
4. The first location in the list of locations is the depot
5. Distance from X to Y is the same as the distance from Y to X

Here is a sample plot of the starting input locations resulting from search query ```McDonalds near Lahore``` with the truck icon showing the depot:

![alt text](https://i.imgur.com/Idm68JF.jpg)

Here is the output and plot created after the algorithm has been run with 3 vehicles as input:
```
Shortest route time: 90.0 minutes
Shortest route is: [[0, 1, 7], [0, 3, 6, 4, 9], [0, 5, 10, 2, 8]]
```

![alt text](https://i.imgur.com/YYUcRBl.jpg)

To try this out, clone the repo and install dependencies (ideally in a virtualenv):

```pip install -r requirements.txt```

Then supply the arguments on command line like this:

```python solution.py <search_query> <number_of_vehicles>```

e.g.

```python solution.py "Sample" 3```

After the first run, your input files will be automatically created and the results dont need to be fetched again. You can add a depot location at the top of the created input file for locations.
