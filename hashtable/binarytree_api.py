#!/usr/bin/env python3


class BinaryTree(object):
    '''
    A binary tree implementation in python.
    '''

    def __init__(self):
        '''
        Creates a binary tree
        '''
        self.root = None

    def _find(self, key, node=None):
        if node is None:
            node = self.root

        if key == node.key:
            return node
        elif key < node.key and node.left is not None:
            return self._find(key, node.left)
        elif key > node.key and node.right is not None:
            return self._find(key, node.right)
        else:
            return None

    def _getMin(self, node):
        '''
        Get the smallest node from the node
        '''
        if node.left is not None:
            return self._getMin(node.left)
        else:
            return node


    def debug_print(self):
        node = self.root

        thislevel = [node]
        all_values = []
        while thislevel:
            nextlevel = list()
            # all_values = all_values + ",".join(n.value for n in thislevel)
            for n in thislevel:
                all_values.append(n.value)
            for n in thislevel:
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            thislevel = nextlevel

        return ", ".join(all_values)

    def set(self,key,value,n=None):
        '''
        Sets a key and value pair in the binary Tree
        '''

        if n is None:
            n = self.root

        if self.root is None:
            self.root = Node(key, value)

        else:
            if key <= n.key:
                if n.left is None:
                    n.left = Node(key, value)
                    n.left.parent = n
                    return
                else:
                    return self.set(key, value, n.left)
            else:
                if n.right is None:
                    n.right = Node(key, value)
                    n.right.parent = n
                    return
                else:
                    return self.set(key, value, n.right)

    def get(self,key):
        '''
        returns the value stored with the given key.  If the key does not exist, null/None should be returned.
        '''
        node = self._find(key)
        return node.value

    def remove(self,key):
        '''
        removes the node with the given key from the tree.  If the key does not exist, it should simply return (no error).
        '''
        node = self._find(key)

        if node is None:
            return

        parent = node.parent

        if node.left is None and node.right is None:
            if key <= parent.key:
                parent.left = None
            else:
                parent.right = None
            return

        if node.left is not None and node.right is None:
            if key <= parent.key:
                parent.left = node.left
                node.left.parent = node.parent
            else:
                parent.right = node.left
                node.right.parent = node.parent
            return

        if node.right is not None and node.left is None:
            if key <= parent.key:
                parent.left = node.right
                node.left.parent = node.parent
            else:
                parent.right = node.right
                node.right.parent = node.parent
            return

        if node.right is not None and node.left is not None:
            min_node = self._getMin(node.right)
            node.key = min_node.key
            node.value = min_node.value
            min_node.parent.left = None
            return


    def walk_dfs_inorder(self, node=None):
        '''
        iterates through the nodes of the tree in depth-first-search "inorder" order.
        '''
        if node is None:
            node = self.root

        if node.left != None:
            self.walk_dfs_inorder(node.left)

        print(node.value)

        if node.right != None:
            self.walk_dfs_inorder(node.right)

    def walk_dfs_preorder(self, node=None):
        '''
        iterates through the nodes of the tree in depth-first-search "inorder" order.
        '''
        if node is None:
            node = self.root

        print(node.value)

        if node.left != None:
            self.walk_dfs_preorder(node.left)

        if node.right != None:
            self.walk_dfs_preorder(node.right)

    def walk_dfs_postorder(self, node=None):
        '''
         iterates through the nodes of the tree in depth-first-search "postorder" order.
        '''
        if node is None:
            node = self.root

        if node.left != None:
            self.walk_dfs_postorder(node.left)

        if node.right != None:
            self.walk_dfs_postorder(node.right)

        print(node.value)

    def walk_bfs(self):
        '''
        iterates through the nodes of the tree in breadth-first-search order.
        '''
        node = self.root

        thislevel = [node]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print (n.value)
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            thislevel = nextlevel


######################################################
###   A node in the binary tree

class Node(object):
    '''A node on the binary tree'''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        if self.parent == None:
            parent = '-'
        else:
            parent = self.parent.key
        return '{}({})'.format(self.key, parent)
