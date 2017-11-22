#!/usr/bin/env python3


class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = []
        self.size = 0 # keep track of how many things are in there to know
        self.initial_size = initial_size
        self.chunk_size = chunk_size
        for i in range(initial_size):
            self.data.append(None)

    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        bound = False
        if 0 <= index <= self.size - 1:
            bound = True
        else:
            raise Exception('Index out of bounds')
        return bound

    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if self.size == self.initial_size:
            newSize = self.initial_size + self.chunk_size
            self.data = alloc(self, newSize)
            self.initial_size += self.chunk_size

    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        newSize = self.initial_size - self.chunk_size
        if self.size <= newSize and self.size > 10:
            self.data = alloc(self, newSize)
            self.initial_size = newSize


    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self._check_increase()
        self.data[self.size] = item
        self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        try:
            self._check_bounds(index)
            self._check_increase()
            self.size += 1

            newArr = []
            for i in range(self.initial_size):
                newArr.append(None)

            for i in range(self.size):
                if i == index:
                    newArr[i] = item
                elif i > index:
                    newArr[i] = self.data[i - 1]
                else:
                    newArr[i] = self.data[i]
            self.data = newArr

        except:
            print('Error: {} is not within the bounds of the current array.'.format(index))


    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        try:
            self._check_bounds(index)
            self.data[index] = item
        except:
            print('Error: {} is not within the bounds of the current array.'.format(index))

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        try:
            self._check_bounds(index)
            print(self.data[index])
        except:
            print('Error: {} is not within the bounds of the current array.'.format(index))

    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        try:
            self._check_bounds(index)
            for i in range(self.size + 1):
                if i == index or i > index and i+1 < self.size:
                    self.data[i] = self.data[i+1]
            self.size -= 1
            self._check_decrease()
        except:
            print('Error: {} is not within the bounds of the current array.'.format(index))

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        try:
            self._check_bounds(index1)
            try:
                self._check_bounds(index2)
                tmp = self.data[index1]
                self.data[index1] = self.data[index2]
                self.data[index2] = tmp
            except:
                print('Error: {} is not within the bounds of the current array.'.format(index2))
        except:
            print('Error: {} is not within the bounds of the current array.'.format(index1))



###################################################
###   Utilities

def alloc(arr, size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    # Create a new array with an increased size
    newArr = []
    for i in range(size):
        newArr.append(None)

    return memcpy(newArr, arr, size)

def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    for i in range(source.size):
        dest[i] = source.data[i]

    return dest
