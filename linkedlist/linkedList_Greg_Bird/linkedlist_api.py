#!/usr/bin/env python3


class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0

    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if index > self.size - 1:
            raise Exception('{} is not within the bounds of the current list.'.format(index))

    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print('{} >>> {}'.format(self.size, ', '.join(values)))


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        for i in range(index):
            n = n.next
        return n

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        n = self.head
        if self.size > 0:
            while n.next is not None:
                n = n.next
            n.next = Node(item)
        else:
            node = Node(item)
            self.head = node
        self.size += 1


    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        self._check_bounds(index)
        n = self._get_node(index - 1)
        node = Node(item)
        # set new node.next = to previous node.next the set old n.next equal to the new node
        node.next = n.next
        n.next = node
        self.size += 1

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        self._check_bounds(index)
        n = self._get_node(index)
        n.value = item

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        self._check_bounds(index)
        n = self._get_node(index)
        return n.value

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        self._check_bounds(index)
        n = self._get_node(index - 1)
        deletedNode = self._get_node(index)
        # Set previous node equal to deleted nodes next value
        n.next = deletedNode.next
        self.size -= 1

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        self._check_bounds(index1)
        self._check_bounds(index2)

        one = self._get_node(index1)
        two = self._get_node(index2)

        temp = one.value
        one.value = two.value
        two.value = temp

######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)
