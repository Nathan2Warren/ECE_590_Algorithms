"""
Math 560
Project 2
Fall 2020

p2stack.py

Partner 1: Nathan Warren (naw32)
Partner 2: Varun Prasad (vp60)
Date: 10/17/20
"""

"""
Stack Class
"""


class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """

    def __init__(self, size=3):
        self.stack = [None for x in range(0, size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """

    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """

    # Check if full
    def isFull(self):
        if self.numElems == len(self.stack):
            return True

    """
    isEmpty function to check if the stack is empty.
    """

    # Check if empty
    def isEmpty(self):
        if self.numElems == 0:
            return True

    """
    resize function to resize the stack by doubling its size.
    """

    # Double the size of the stack
    def resize(self):
        new_stack = [None for i in range(0, self.numElems*2)]
        new_stack[0: self.numElems] = self.stack
        self.stack = new_stack
        return

    """
    push function to push a value onto the stack.
    """

    # Check if resize is needed, then add value to top of stack
    def push(self, val):
        if self.isFull():
            self.resize()
        self.stack[self.numElems] = val
        self.numElems += 1
        self.top += 1
        return

    """
    pop function to pop the value off the top of the stack.
    """

    # If list is not empty then remove the last value and store it as popped
    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped = self.stack[self.top]
            self.stack[self.top] = None
            self.numElems -= 1
            self.top -= 1
            return popped
