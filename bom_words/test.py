#!/usr/bin/env python3
import unittest
from bubblesort_api import bubble_sort
from worddata import WordData
from insertionsort_api import insertion_sort
from selectionsort_api import selection_sort

class TestBubbleSort(unittest.TestCase):

    def test_bubblesort(self):
        my_list = []
        my_list.append(WordData('book', 'test', 1, 2.2))
        my_list.append(WordData('book', 'test', 2, 2.3))
        my_list.append(WordData('book', 'test', 3, 2.4))
        my_list.append(WordData('book', 'test', 4, 2.5))
        my_list.append(WordData('book', 'test', 5, 2.6))

        sortedList = bubble_sort(my_list, 'percent')


        self.assertEqual(sortedList[0].percent, 2.2)


    def test_insertionsort(self):
        my_list = [12, 5, 13, 8, 9, 65]
        good_list = [5, 8, 9, 12, 13, 65]

        sortedList = insertion_sort(my_list)

        self.assertEqual(sortedList, good_list)

    def test_selectionsort(self):
        my_list = [12, 5, 13, 8, 9, 65]
        good_list = [5, 8, 9, 12, 13, 65]

        sortedList = selection_sort(my_list)

        self.assertEqual(sortedList, good_list)

if __name__ == '__main__':
    unittest.main()
