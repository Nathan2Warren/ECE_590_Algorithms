"""
Math 560
Project 3
Fall 2020

Partner 1: Varun Prasad (vp60)
Partner 2: Nathan Warren (naw32)
Date: October 29, 2020
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage

This function will first use the Bellman-Ford algorithm to update edges around
the graph of exchange rates for N - 1 iterations, where N is the number of
vertices. After performing one more iteration, it will detect if any additional
updates are made, indicating a negative cost cycle is present.
It will then identify the path of negative cost cycle to indicate that
there is an arbitrage opportunity.

INPUTS
adjList: the adjacency list of Vertex objects
adjMat:  the adjacency matrix (stored as a 2D list)
tol: tolerance value for updating

OUTPUTS
neg_cycle: The path of vertices that represent a negative cost cycle
"""


def detectArbitrage(adjList, adjMat, tol=1e-15):
    # Initialize vertex distances and previous vakyes
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None
    adjList[0].dist = 0

    # Initialize list and values for negative cost cycle
    neg_cycle = []
    start = None
    start_prev = None

    # Perform Bellman-Ford algorithm, iterating 1 less time than number of
    # vertices
    for iter in range(len(adjList) - 1):
        # Look at each vertex
        for v in adjList:
            # Check each neighbor of the vertex and update prediction and
            # previous vertex
            for n in v.neigh:
                # Only update if the new value is better!
                if n.dist > v.dist + adjMat[v.rank][n.rank] + tol:
                    n.dist = v.dist + adjMat[v.rank][n.rank]
                    n.prev = v

    # Perform one more iteration to detect negative cost cycle
    # by seeing if any vertex changes
    for v in adjList:
        # Check each neighbor of the vertex and update prediction and
        # previous vertex
        for n in v.neigh:
            # Check if a neighbor's distance updates and break the loop
            # to begin tracing the negative cost cycle from this vertex
            if n.dist > v.dist + adjMat[v.rank][n.rank] + tol:
                start = v
                start_prev = start.prev
                break

    # Determine negative cost cycle path if there is one
    if start:
        # Add the starting vertex to the cycle
        neg_cycle.append(start.rank)
        # Cycle through vertices until starting point is reached
        while start_prev.rank != start.rank:
            # Append previous vertex to the list
            neg_cycle.append(start_prev.rank)

            # Update start_prev
            start_prev = start_prev.prev
        # Add starting vertex to complete the cycle
        neg_cycle.append(start.rank)

    # Return negative cost cycle
    return neg_cycle[::-1]

################################################################################


"""
rates2mat

This function will create an adjacency matrix of the exchange rates of different
currencies. Using this function will be key for detecting arbitrage.

INPUTS
rates: 2D ist representing the exchange rates

OUTPUTS
negative log of the exchange rates for proper use in arbitrage detection
"""

def rates2mat(rates):
    # Returns negative log of rates as our edge weights
    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
