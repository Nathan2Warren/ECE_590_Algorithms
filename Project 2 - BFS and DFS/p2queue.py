"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1: Nathan Warren (naw32)
Partner 2: Varun Prasad (vp60)
Date: 10/17/20
"""

"""
Queue Class
"""


class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """

    def __init__(self, size=3):
        self.queue = [None for x in range(0, size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """

    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    # Check if full

    def isFull(self):
        if self.numElems == len(self.queue):
            return True

    """
    isEmpty function to check if the queue is empty.
    """
    # Check if empty

    def isEmpty(self):
        if self.numElems == 0:
            return True

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    # Double the size of the stack

    def resize(self):
        new_queue = [None for i in range(0, self.numElems * 2)]
        if self.rear <= self.front:
            j = 0

            for i in range(0, self.rear):
                new_queue[j] = self.queue[i]
                j += 1
            for k in range(len(self.queue)):
                new_queue[j] = None
                j += 1
            for l in range(self.rear, len(self.queue)):
                new_queue[j] = self.queue[l]
                j += 1
            self.front += len(self.queue)
        else:
            new_queue[0: self.numElems] = self.queue
        self.queue = new_queue

        return

    """
    push function to push a value into the rear of the queue.
    """
    # Check if resize is needed, then add value to top of stack

    def push(self, val):
        if self.isFull():
            self.resize()

        if self.rear >= len(self.queue) and self.queue[0] == None:
            self.rear = 0

        self.queue[self.rear] = val
        self.rear += 1
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    # If list is not empty then remove the last value and store it as popped

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            self.numElems -= 1
            if self.front >= len(self.queue):
                self.front = 0
        return popped
