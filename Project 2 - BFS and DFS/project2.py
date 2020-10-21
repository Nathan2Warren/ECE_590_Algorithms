"""
Math 560
Project 2
Fall 2020

project2.py

Partner 1: Nathan Warren (naw32)
Partner 2: Varun Prasad (vp60)
Date: 10/17/20
"""

# Import math and other p2 files.
import math
from p2tests import *
from p2queue import *
from p2stack import *
from p2maze import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # Conduct BFS
    if alg == 'BFS':
        # Initialize path as empty list
        path = []

        # For all vertices, reinitialize visited to False and previous to None
        for i in maze.adjList:
            i.visited = False
            i.prev = None

        # Create queue
        queue = Queue()

        # Push start into queue and indicate as visited
        queue.push(maze.start)
        maze.start.visited = True

        # Run loop while queue is not empty
        while not queue.isEmpty():
            # Obtain current Vertex
            current = queue.pop()

            # Break if exit is reached
            if current == maze.exit:
                path.append(maze.exit.rank)
                # Trace shortest path back through the maze
                while current.prev is not None:
                    previous = current.prev
                    path.append(previous.rank)
                    current = current.prev
                break

            # Check neighbors, initializing previous and visited values
            for n in current.neigh:
                if n.visited == False:
                    queue.push(n)
                    n.prev = current
                    n.visited = True
    # Conduct DFS
    if alg == 'DFS':
        # Initialize path
        path = []

        # For all vertices, reinitialize visited to False and previous to None
        for i in maze.adjList:
            i.visited = False
            i.prev = None

        # Create stack
        stack = Stack()

        # Push start into stack and indicate as visited
        stack.push(maze.start)
        maze.start.visited = True

        # Run loop while stack is not empty
        while not stack.isEmpty():
            # Obtain current Vertex
            current = stack.pop()

            # Break if exit is reached
            if current == maze.exit:
                path.append(maze.exit.rank)
                # Trace shortest path back through the maze
                while current.prev is not None:
                    previous = current.prev
                    path.append(previous.rank)
                    current = current.prev
                break

            # Check neighbors, initializing previous and visited values
            for n in current.neigh:
                if n.visited == False:
                    stack.push(n)
                    n.prev = current
                    n.visited = True

    # Return shortest path
    return path[::-1]


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)
