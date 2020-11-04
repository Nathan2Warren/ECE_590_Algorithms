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
    # Create dynamic programming table (2D list)
    rows, cols = len(src) + 1, len(dest) + 1
    table = [[0 for i in range(rows)] for j in range(cols)]

    # Fill in the first row and first column of the table
    for i in range(rows):
        for j in range(cols):
            # Base case: 1st string empty so insert all characters from 2nd
            if i == 0:
                table[i][j] = j
            # Base case: 2nd string empty so delete all characters from 1st
            elif j == 0:
                table[i][j] = i
    for row in table:
        print(row)

    # Fill in the rest of the table
    for i in range(1,rows):
        for j in range(1,cols):
            # If letters are the same, copy the diagonal
            if src[i-1] == dest[j-1]:
                table[i][j] = table[i-1][j-1]
            # If not compute insertion, deletion, substitution
            else:
                ins = table[i][j-1]
                delet = table[i-1][j]
                sub = table[i-1][j-1]
                table[i][j] = 1 + min([ins, delet, sub])

    for row in table:
        print(row)


    dist = 0 # This is a placeholder, remove and implement!
    edits = [] # This is a placeholder, remove and implement!
    return dist, edits

################################################################################
ED('', 'abc')


"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300)
    print()
    compareRandStrings(True, 30, 300)
