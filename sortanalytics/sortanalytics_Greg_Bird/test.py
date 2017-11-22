#!/usr/bin/env python3
import unittest
from bubblesort_api import bubble_sort
from insertionsort_api import insertion_sort
from selectionsort_api import selection_sort
from quicksort_api import quick_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubblesort(self):
        my_list = [12, 5, 13, 8, 9, 65]
        good_list = [5, 8, 9, 12, 13, 65]

        sortedList = bubble_sort(my_list)


        self.assertEqual(sortedList, good_list)


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

    def test_quicksort(self):
        my_list = [12, 5, 13, 8, 9, 65]
        good_list = [5, 8, 9, 12, 13, 65]

        quick_sort(my_list, 0, len(my_list) - 1)

        self.assertEqual(my_list, good_list)

    def test_quicksort_already_sorted(self):
        my_list = [5, 8, 9, 12, 13, 65]
        good_list = [5, 8, 9, 12, 13, 65]

        quick_sort(my_list, 0, len(my_list) - 1)

        self.assertEqual(my_list, good_list)

    def test_quicksort_largerList(self):
        my_list = [12, 5, 13, 8, 9, 65, 200, 40, 35, 200, 100, 140]
        sorted_list = [5, 8, 9, 12, 13, 35, 40, 65, 100, 140, 200, 200]

        quick_sort(my_list, 0, len(my_list) - 1 )

        self.assertEqual(my_list, sorted_list)

if __name__ == '__main__':
    unittest.main()
