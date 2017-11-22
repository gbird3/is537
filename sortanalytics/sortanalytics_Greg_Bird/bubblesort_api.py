#!/usr/bin/env python3

def bubble_sort(list, REVERSE=False):
    '''
    A python implementation of bubble sort
    '''

    length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if REVERSE:
                if list[i] < list[i+1]:
                    sorted = False
                    list[i], list[i+1] = list[i+1], list[i]
            else:
                if list[i] > list[i+1]:
                    sorted = False
                    list[i], list[i+1] = list[i+1], list[i]
    return list
