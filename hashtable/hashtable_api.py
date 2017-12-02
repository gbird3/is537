#!/usr/bin/env python3
from abc import ABC, abstractmethod
from numbers import Number
import base64

from binarytree_api import BinaryTree

class Hashtable(ABC):
    def __init__(self):
        '''
        Initiates a hashtable using a binary tree as each bucket
        '''
        self.buckets = []
        for i in range(10):
            tree = BinaryTree()
            self.buckets.append(tree)

    def set(self, key, value):
        '''
        Sets a value in the hashtable based off of the hash
        '''
        hashKey = self.get_hash(key)
        self.buckets[hashKey].set(key, value)

    def get(self, key):
        '''
        Gets the value of the item in the hashtable based of the hash
        '''
        return self.buckets[self.get_hash(key)].get(key)

    def remove(self, key):
        '''
        Removes a value from the hashtable based off the hash.
        '''
        self.buckets[self.get_hash(key)].remove(key)

    def debug_print(self):
        for i in range(len(self.buckets)):
            values = self.buckets[i].debug_print()
            print('{}: {}'.format(i, values))

    @abstractmethod
    def get_hash(self, key):
        pass

class StringHashTable(Hashtable):
    def get_hash(self, key):
        isum = 0
        for c in key:
            isum = isum + ord(c)
        return isum % 10

class GuidHashTable(Hashtable):
    def get_hash(self, key):
        isum = 0
        for c in key:
            if isinstance(c, Number):
                if isum is not 0:
                    isum = isum * c
                else:
                    isum = c
            else:
                isum = isum + ord(c)
        return isum % 10

class ImageHashTable(Hashtable):
    def get_hash(self, key):
        with open('images/' + key, "rb") as imageFile:
            # Read the whole file at once
            str = imageFile.read()
            return len(str) % 10
