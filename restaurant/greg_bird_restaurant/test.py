#!/usr/bin/env python3
import unittest
from circularlist_api import CircularLinkedList
from doublylinkedlist_api import DoublyLinkedList
from queue_api import Queue
from stack_api import Stack

class TestCircularList(unittest.TestCase):

    def setUp(self):
        self.circle = CircularLinkedList()

    def tearDown(self):
        del self.circle

    def test_add(self):
        self.circle.add('Foo')
        node = self.circle._get_node(1)
        # Check if the new node contains the right value.
        self.assertEqual(node.value, 'Foo')
        # Check if the new node.next is equal to the first node
        self.assertEqual(node.next, node)

    def test_insert(self):
        self.circle.add('Foo')
        self.circle.insert(1, '2')

        value = self.circle.get(2)
        self.assertEqual(value, 'Foo')

    def test_set(self):
        self.circle.add('Foo')
        self.circle.set(1, 'Bar')

        value = self.circle.get(1)
        self.assertEqual(value, 'Bar')

    def test_get(self):
        self.circle.add('Foo')
        value = self.circle.get(1)
        self.assertEqual(value, 'Foo')

        self.circle.add('Boo')
        value = self.circle.get(2)
        self.assertEqual(value, 'Boo')

    def test_delete(self):
        self.circle.add('Foo')
        self.circle.add('Bar')
        self.circle.add('FooBar')

        self.circle.delete(2)

        value = self.circle.get(2)
        self.assertEqual(value, 'FooBar')

        self.circle.delete(1)
        value = self.circle.get(1)
        self.assertEqual(value, 'FooBar')

    def test_swap(self):
        self.circle.add('Foo')
        self.circle.add('Bar')
        self.circle.add('FooBar')

        self.circle.swap(1, 3)

        value = self.circle.get(1)
        self.assertEqual(value, 'FooBar')

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.double = DoublyLinkedList()

    def tearDown(self):
        del self.double

    def test_add(self):
        ''' Test Adding a value to the list '''
        self.double.add("A")
        self.double.add("B")
        self.double.add("C")
        value = self.double._get_node(1)
        self.assertEqual(value.value, 'B')

    def test_insert(self):
        ''' Test Adding a value to the list '''
        self.double.add("A")
        self.double.add("B")
        self.double.add("C")
        self.double.insert(0, '2')

        value = self.double._get_node(0)
        self.assertEqual(value.value, '2')

    def test_get(self):
        ''' Test getting a value of a specific index '''
        self.double.add("A")
        self.double.add("B")
        self.double.add("C")

        value = self.double.get(2)
        self.assertEqual(value, 'C')

    def test_delete(self):
        self.double.add('A')
        self.double.add('B')
        self.double.add('C')

        self.double.delete(0)

        value = self.double.get(0)

        self.assertEqual(value, 'B')

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        del self.queue

    def test_enqueue(self):
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')

        value = self.queue.dequeue()
        self.assertEqual(value, 'A')

    def test_dequeue(self):
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')

        value1 = self.queue.dequeue()
        value2 = self.queue.dequeue()

        self.assertEqual(value1, 'A')
        self.assertEqual(value2, 'B')

    def test_size(self):
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')

        size = self.queue.size()

        self.assertEqual(size, 3)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push('A')
        value = self.stack.get(0)

        self.assertEqual(value, 'A')

    def test_pop(self):
        self.stack.push('A')
        self.stack.push('B')
        value = self.stack.pop()
        self.assertEqual(value, 'B')

if __name__ == '__main__':
    unittest.main()
