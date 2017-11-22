import unittest
from circularlist_api import CircularLinkedList

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

if __name__ == '__main__':
    unittest.main()
