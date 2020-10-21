"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1: Nathan Warren (naw32)
Partner 2: Varun PraSAD (vp60)
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

    def isFull(self):
        if self.numElems == len(self.queue):
            return True

    """
    isEmpty function to check if the queue is empty.
    """

    def isEmpty(self):
        if self.numElems == 0:
            return True

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """

    def resize(self):
        new_queue = [None for i in range(0, self.numElems * 2)]
        new_queue[0: self.numElems] = self.queue
        self.queue = new_queue

        return

    """
    push function to push a value into the rear of the queue.
    """

    def push(self, val):
        if self.isFull():
            self.resize()
        self.queue[self.rear] = val
        self.rear += 1
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped = self.queue[self.front]
            self.queue[self.front] = None
            self.numElems -= 1
            shifted = [None for i in range(0, len(self.queue))]
            j = 0
            for i in self.queue:
                if i != None:
                    shifted[j] = i
                    j += 1
            self.rear -= 1
            self.queue = shifted
        return popped


queue = Queue()
queue.queue
queue.push(1)
queue.queue
queue.push(2)
queue.push(3)
queue.queue
queue.push(4)
queue.queue
queue.pop()
queue.queue
queue.pop()
queue.queue
queue.push(5)
queue.push(6)
queue.queue
queue.push(7)
queue.queue
queue.push(8)
queue.queue
queue.push(9)
queue.queue
queue.push(10)
queue.queue
