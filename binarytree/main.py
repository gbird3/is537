import unittest
from binarytree_api import BinaryTree


tree = BinaryTree()

tree.set('c', 'C')
tree.set('h', 'H')
tree.set('a', 'A')
tree.set('e', 'E')
tree.set('f', 'F')
tree.set('d', 'D')
tree.set('b', 'B')
tree.set('j', 'J')
tree.set('g', 'G')
tree.set('i', 'I')
tree.set('k', 'K')

print('Initial tree:')
tree.debug_print()

print('\nLookups:')
print(tree.get('f'))
print(tree.get('b'))
print(tree.get('i'))

print('\nBFS:')
tree.walk_bfs()

print('\nDFS preorder:')
tree.walk_dfs_preorder()

print('\nDFS inorder:')
tree.walk_dfs_inorder()

print('\nDFS postorder:')
tree.walk_dfs_postorder()

print('\nRemove b:')
tree.remove('b')
tree.debug_print()

print('\nRemove f:')
tree.remove('f')
tree.debug_print()

print('\nRemove h:')
tree.remove('h')
tree.debug_print()
