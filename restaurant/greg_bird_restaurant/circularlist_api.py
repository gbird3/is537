#!/usr/bin/env python3

class CircularLinkedList(object):
    '''
    A circularly-linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0

    def debug_print(self):
        '''Prints a representation of the entire list.'''
        values = []
        n = self.head
        i = 0
        while i < self.size:
            values.append(str(n.value))
            n = n.next
            i += 1
        print('{} >>> {}'.format(self.size, ', '.join(values)))

    def debug_cycle(self, count):
        '''Prints a representation of the entire cycled list up to count items'''
        values = []
        n = self.head
        for j in range(count):
            i = 0
            while i < self.size:
                values.append(str(n.value))
                n = n.next
                i += 1
            j+=1
        print('{} >>> {}'.format(self.size, ', '.join(values)))

    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if index > self.size:
            raise Exception('{} is not within the bounds of the current list.'.format(index))

    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        n = self.head
        for i in range(index - 1):
            if i != self.size:
                n = n.next
        return n

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        n = self.head
        node = Node(item)
        if self.size > 0:
            i = 1
            while i < self.size:
                n = n.next
                i += 1
            first_node = n.next
            node.next = first_node
            n.next = node
        else:
            node.next = node
            n = node
            self.head = n
        self.size += 1

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right.'''
        self._check_bounds(index)
        if index == 1:
            # set last node.next equal to new first node.
            last = self._get_node(self.size)
            first = self._get_node(1)
            node = Node(item)
            node.next = first
            last.next = node
            self.head = node
        else:
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
        deletedNode = self._get_node(index)
        if index == 1:
            # Get the last node and set that node.next to node(2)
            last = self._get_node(self.size)
            self.head = deletedNode.next
            last.next = deletedNode.next
        else:
            n = self._get_node(index - 1)
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



######################################################
###   An iterator for the circular list

class CircularLinkedListIterator(object):
    def __init__(self, circular_list):
        '''Starts the iterator on the given circular list.'''
        self.position = 0
        self.list = circular_list.head

    def has_next(self):
        '''Returns whether there is another value in the list.'''
        has_next = False
        n = self.list
        i = 0
        if n is not None:
            while i <= self.position:
                n = n.next
                i += 1
            if n.next is not None:
                has_next = True

        return has_next

    def next(self):
        '''Returns the next value, and increments the iterator by one value.'''
        n = self.list
        i = 0
        while i < self.position:
            n = n.next
            i += 1
        self.position += 1
        return n.value
