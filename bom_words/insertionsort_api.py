#!/usr/bin/env python3

def insertion_sort(list):
    '''
    A python implementation of insertion sort
    '''

    for i in range(1, len(list)):
        item = list[i]

        j = i - 1
        while j >= 0 and item < list[j]:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = item

    return list
