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
ED: the edit distance function
"""


def ED(src, dest):
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
    output = []
    # Traceback the optimal solution
    while (r != 0) and (c != 0):
        if src[r-1] == dest[c-1]:
            r -= 1
            c -= 1
            output.append(('match', src[r], r))
        else:
            move_dir = {"sub": table[r-1][c-1], "delete": table[r-1][c], "insert": table[r][c-1]}

            val_list = list(move_dir.values())
            key_list = list(move_dir.keys())

            move_val = min(val_list)
            move_key = key_list[val_list.index(move_val)]

            if move_key == "sub":
                r -= 1
                c -= 1
                output.append((move_key, dest[c], r))
            elif move_key == "delete":
                r -= 1
                output.append((move_key, src[r], r))
            else:
                c -= 1
                output.append((move_key, dest[c], r))
    while r != 0:
        r -= 1
        output.append(('delete', src[r], r))
    while c != 0:
        c -= 1
        output.append(('insert', dest[c], r))
    dist = table[-1][-1]
    return dist, output


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
