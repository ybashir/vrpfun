# A pythonic but brute-force solution for the Vehicle Routing Problem (VRP)

VRP is a generalized version of the Traveling Salesperson Problem.

This is a brute-force solution to the VRP which finds an optimal route given a depot, a set of delivery locations and the number of vehicles starting from the depot.

The program takes a google maps search resulting in a list of locations and the number of vehicles as input and outputs optimal routes for those vehicles. There are a few simplistic assumptions:

1. Vehicles have infinite capacity
2. Each delivery location needs to be visited just once
3. Vehicles come back to the depot
4. The first location in the list of locations is the depot

Here is a sample plot of the starting input locations with the truck icon showing the depot:

![alt text](https://i.imgur.com/Idm68JF.jpg)

Here is the output and plot created after the algorithm has been run with 3 vehicles as input:
```
Shortest route time: 90.0 minutes
Shortest route is: [[0, 1, 7], [0, 3, 6, 4, 9], [0, 5, 10, 2, 8]]
```

![alt text](https://i.imgur.com/YYUcRBl.jpg)
