"""
Math 560
Project 5
Fall 2020

Partner 1: Nathan Warren (naw32)
Partner 2: Varun Prasad (vp60)
Date:
"""

# Import math, itertools, and time.
from p5tests import *
import math
import itertools
import time
import random

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""


def prim(adjList, adjMat):
    # Initialize all costs to inf and prev to none
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None

    # Pick an arbitrary start vertex and set cost to 0
    start = random.choice(adjList), start.cost = 0

    # Make the priority queue using cost for sorting
    Q = PriorityQueue(adjList)

    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it
        v = Q.delete.min(), v.visited = True

        # For each edge out of v
        for neighbor in v.neigh:
            # If the edge leads out, update
            if not neighbor.visited:
                if neighbor.cost > adjMat[v][neighbor]:
                    neighbor.cost = adjMat[v][neighbor]
                    neighbor.prev = v

################################################################################


"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""


def kruskal(adjList, edgeList):
    # Initialize all singleton sets for each vertex
    for vertex in adjList:
        makeset(vertex)
    # Initialize empty MST
    X = []

    # Loop through the edges in increasing order
    for e in edgeList:
        # If the min edge crosses a cut, add it to our MST
        u, v = e.vertices

        if find(u) != find(v):
            X.append(e)
            union(u, v)
    return X


################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""


def makeset(v):
    v.pi = v
    v.height = 0


"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""


def find(v):
    while v != v.pi:
        v = v.pi
    return v.pi


"""
union: this function will union the sets of vertices v and u.
"""


def union(u, v):
    # union by height
    # make the root of one point to the root of the other.
    # Find root of the tree for u
    ru = find(u)
    rv = find(v)

    # If the sets are already the same, return
    if ru == rv:
        return

    if ru.height > rv.height:
        rv.pi = ru

    elif ru.height < rv.height:
        ru.pi = rv

    else:
        # Same height, break tie
        ru.pi = rv

        # Tree got taller, increment rv.height
        rv.height += 1
    return

################################################################################


"""
TSP
"""


def tsp(adjList, start):

    tour = []
    return tour

################################################################################


# Import the tests (since we have now defined prim and kruskal).

"""
Main function.
"""
if __name__ == "__main__":
    verb = False  # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
