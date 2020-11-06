"""
Math 560
Project 4
Fall 2020

Partner 1: Varun Prasad (vp60)
Partner 2: Nathan Warren (naw32)
Date: Nov 6, 2020
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function. This function will use dynamic programming to
determine the number of steps required to convert one string to another. A
table will first be created, and the optimal edit solution will be traced
back through the table. The specific steps for conversion will also be listed.

Inputs:
src: the source string
dest: the string to which src must be converted

Outputs:
edits: a list that contains the specific edit step (e.g. 'insert'), the
character that is edited, and the index of the character in the original string
dist: the minimum number of edits to convert src to dest
"""


def ED(src, dest):
    # Initialize distance and edit list
    dist = 0
    edits = []

    # Create dynamic programming table (2D list)
    rows, cols = len(src) + 1, len(dest) + 1
    table = [[0 for j in range(cols)] for i in range(rows)]
    # Fill in the first row and first column of the table
    for i in range(rows):
        for j in range(cols):
            # Base case: 1st string empty so insert all characters from 2nd
            if i == 0:
                table[i][j] = j
            # Base case: 2nd string empty so delete all characters from 1st
            elif j == 0:
                table[i][j] = i

    # Fill in the rest of the table
    for i in range(1, rows):
        for j in range(1, cols):
            # If letters are the same, copy the diagonal
            if src[i-1] == dest[j-1]:
                table[i][j] = table[i-1][j-1]
            # If not compute insertion, deletion, substitution
            else:
                ins = table[i][j-1]
                delet = table[i-1][j]
                sub = table[i-1][j-1]
                table[i][j] = 1 + min([ins, delet, sub])
    # Backtrace from the optimal solution
    r, c = len(src), len(dest)

    # Traceback the edits from the optimal solution
    while (r != 0) and (c != 0):
        # If letters are equivalent, return 'match'
        if src[r-1] == dest[c-1]:
            r -= 1
            c -= 1
            edits.append(('match', src[r], r))
        else:
            # Else return appropriate edit
            # Create list of edits and adjacent values
            edit_list = ['sub', 'delete', 'insert']
            val_list = [table[r-1][c-1], table[r-1][c], table[r][c-1]]

            # Identify index of minimum value and find corresponding edit
            move_val_index = val_list.index(min(val_list))
            move_key = edit_list[move_val_index]

            # Add specific edit to list based on determined min step
            if move_key == "sub":
                r -= 1
                c -= 1
                edits.append((move_key, dest[c], r))
            elif move_key == "delete":
                r -= 1
                edits.append((move_key, src[r], r))
            else:
                c -= 1
                edits.append((move_key, dest[c], r))

    # Consider base case of being along left column (all deletions)
    while r != 0:
        r -= 1
        edits.append(('delete', src[r], r))

    # Consider base case of being along top row (all insertions)
    while c != 0:
        c -= 1
        edits.append(('insert', dest[c], r))

    # Calculate the total number of edits required
    dist = table[-1][-1]
    return dist, edits


################################################################################
"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
