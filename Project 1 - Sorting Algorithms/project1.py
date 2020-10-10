"""
Math 560
Project 1
Fall 2020

Partner 1: Nathan Warren (naw32)
Partner 2: Varun Prasad (vp60)
Date: 10/09/2020
"""
from project1tests import *
"""
SelectionSort

Purpose: This function will sort an list using Selection Sort. It will effectively
break the list into a sorted and unsorted portion. It will find the minimum
element in the unsorted section and place it at the end of the sorted section.
This process will repeat until all elements are sorted.

INPUTS
listToSort: the original unsorted list

OUTPUTS
listToSort: the list sorted in place
"""


def SelectionSort(listToSort):
    # Specify partition of list to inspect (unsorted region)
    for i in range(len(listToSort)):
        #  Loop through all pairs of elements in the unsorted portion
        for j in range(i, len(listToSort)):
            # Swap the first element in the unsorted portion with the minimum
            if listToSort[j] < listToSort[i]:
                listToSort[j], listToSort[i] = listToSort[i], listToSort[j]
    return listToSort


"""
InsertionSort

Purpose: This function will sort an list using Insertion Sort. It will effectively
break the list into a sorted and unsorted portion. It will compare
an element in the unsorted portion with the preceding element in the sorted
portion. If the element is less than an element in the sorted portion, it will
swap the two (reverse bubble). This process will continue until a pair of
elements cannot be swapped, resulting in a sorted list.

INPUTS
listToSort: the original unsorted list

OUTPUTS
listToSort: the list sorted in place

"""


def InsertionSort(listToSort):
    # Iterate over the list
    for i in range(1, len(listToSort)):
        # Create index that starts from the preceding element
        j = i - 1
        # Compare previous element with current one
        while (listToSort[j] > listToSort[i] and j >= 0):
            # Swap elements if preceding element is larger than current one
            listToSort[i], listToSort[j] = listToSort[j], listToSort[i]
            # Decrement indices until condition is no longer met (cannot swap)
            j -= 1
            i -= 1
    return listToSort


"""
BubbleSort

Purpose: This function will sort an list using Bubble Sort. Per cycle, defined
as one full pass through the list, the algorthim will compare pairs of adjacent
elements. If the elements are in incorrect order, they will be swapped. After
each cycle, the range of search excludes an additional element at the end of the
list since those elements have been sorted.

INPUTS
listToSort: the original unsorted list

OUTPUTS
listToSort: the list sorted in place
"""


def BubbleSort(listToSort):
    # Cycle counter: one cycle is one full pass through the list
    for i in range(len(listToSort)):
        # Create boolean that determines if the list is already sorted (assume True)
        sorted = True
        # Per cycle, iterate through list and compare adjacent pairs of elements
        for j in range(0, len(listToSort)-1-i):  # Exclude sorted portion
            # If element at higher index is smaller, swap elements
            if listToSort[j] > listToSort[j+1] and j+1 <= len(listToSort):
                listToSort[j], listToSort[j+1] = listToSort[j+1], listToSort[j]
                # Set sorted to false since 2 elements were swapped
                sorted = False
        # Break loop if no items were swapped
        if sorted == True:
            break;

    return listToSort

"""
MergeSort

Purpose: This function will sort an list using Merge Sort. This algorithm will
break down lists into single element lists recursively. It will then compare
each element to elements in the adjacent lists and then pair them up and sort
them recursively.

INPUTS
listToSort: the original unsorted list

OUTPUTS
listToSort: a new list that is sorted
"""


def MergeSort(listToSort):
    # Find midpoint and split list in half if list size is larger than 1
    if len(listToSort) > 1:
        mid = len(listToSort)//2
        left = listToSort[:mid]
        right = listToSort[mid:]
        # Recursively sort the halves
        MergeSort(left)
        MergeSort(right)
        # Create variables that can be used to increment from the left, right,
        # and sorted list indicies
        i = 0
        j = 0
        k = 0
        # Look at the ith and jth element from the left and right list and add
        # the lower number to the sorted list first
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                listToSort[k] = left[i]
                i += 1
                k += 1
                pass
            else:
                listToSort[k] = right[j]
                j += 1
                k += 1
        # Copy remaining elements in left and right if there are any
        while i < len(left):
            listToSort[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            listToSort[k] = right[j]
            j += 1
            k += 1
    return listToSort


"""
QuickSort

Purpose: This function will sort an list using Quick Sort. This algorithm sets
the last number in the list to be the pivot. Elements in the list are then sorted
based on their value compared to the value of the pivot. It does this by using
two pointers: i, which starts at the start of the list and j, which starts one
position left of the pivot index. i is incremented towards the center of the list
if i <= pivot till a value greater than the pivot is found. j is also incremented
towards the center of the list if j >= the pivot value, until a value smaller
than the pivot is found. If both pointers stop moving, the elements in the list
that they point at will switch positions. Once the pointers meet, the pivot
element will be moved to the index where i points. This process will be
repeated recursively until the list is sorted.

INPUTS
listToSort: the original unsorted list

OUTPUTS
listToSort: the list sorted in place
"""


def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None or j == len(listToSort):
        j = len(listToSort) - 1
    # If i pointer is greater than or equal to j pointer, return the sorted list
    if i >= j:
        return listToSort
    # Create variables to store initial starting and ending points
    start = i
    end = j
    # Pivot will always be the last number in the list
    pivot = j
    # Pointer j will start at one number left of the pivot
    j -= 1

    # Continue repeating this incrementing code as long as i is less than or
    # equal to j
    while i <= j:
        # If the number at index i is less than the pivot, then increment i by 1
        while listToSort[i] <= listToSort[pivot] and i <= j:
            i += 1
        # If the number at index j is more than the pivot, then increment j by 1
        while listToSort[j] >= listToSort[pivot] and i <= j:
            j -= 1
        # Swap places of the numbers if the number at index i is greater than
        # the number at index j
        if i <= j:
            listToSort[i], listToSort[j] = listToSort[j], listToSort[i]
    # Move pivot to correct position (all items left of pivot are smaller than
    # the pivot and all items right of the pivot are greater than the pivot)
    listToSort[pivot], listToSort[i] = listToSort[i], listToSort[pivot]
    # Recursively repeat this process till i >= j
    QuickSort(listToSort, start, j)
    QuickSort(listToSort, j+1, end)
    return listToSort


"""
Importing the testing code after function defs to ensure same references.
"""

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('DEFAULT measureTime')
    print()
    measureTime(preSorted = True)
