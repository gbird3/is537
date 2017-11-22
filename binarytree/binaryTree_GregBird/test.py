import unittest
from binarytree_api import BinaryTree

class TestToJson(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def testSet(self):
        self.tree.set('f', 'F')
        self.tree.set('g', 'G')
        self.tree.set('a', 'A')

        value1 = self.tree.get('f')
        value2 = self.tree.get('g')
        value3 = self.tree.get('a')


        self.assertEqual(value1, 'F')
        self.assertEqual(value2, 'G')
        self.assertEqual(value3, 'A')

    def test_remove(self):
        self.tree.set('f', 'F')
        self.tree.set('g', 'G')
        self.tree.set('a', 'A')
        self.tree.set('b', 'B')
        self.tree.set('c', 'C')
        self.tree.set('d', 'D')
        self.tree.set('e', 'E')
        self.tree.set('h', 'H')
        self.tree.set('i', 'I')

        self.tree.remove('c')

        self.assertEqual(self.tree._find('f').__str__(), 'f(-)')
        self.assertEqual(self.tree._find('a').__str__(), 'a(f)')

    def test_find(self):
        self.tree.set('f', 'F')
        self.tree.set('g', 'G')
        self.tree.set('a', 'A')

        node = self.tree.get('a')
        self.assertEqual(node, 'A')

    def test_get(self):
        self.tree.set('f', 'F')
        self.tree.set('g', 'G')
        self.tree.set('a', 'A')

        value = self.tree.get('g')

        self.assertEqual(value, 'G')


if __name__ == '__main__':
    unittest.main()
