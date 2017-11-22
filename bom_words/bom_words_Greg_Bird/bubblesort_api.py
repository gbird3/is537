#!/usr/bin/env python3

def bubble_sort(list, key, REVERSE=False):
    '''
    A python implementation of bubble sort
    '''

    length = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if REVERSE:
                if list[i].percent < list[i+1].percent:
                    sorted = False
                    list[i], list[i+1] = list[i+1], list[i]
                elif list[i].percent == list[i+1].percent:
                    if list[i].count < list[i+1].count:
                        list[i], list[i+1] = list[i+1], list[i]
                    elif list[i].count == list[i+1].count:
                        if list[i].word > list[i+1].word:
                            list[i], list[i+1] = list[i+1], list[i]
            else:
                if list[i].percent > list[i+1].percent:
                    sorted = False
                    list[i], list[i+1] = list[i+1], list[i]
                elif list[i].percent == list[i+1].percent:
                    if list[i].count < list[i+1].count:
                        list[i], list[i+1] = list[i+1], list[i]
                    elif list[i].count == list[i+1].count:
                        if list[i].word > list[i+1].word:
                            list[i], list[i+1] = list[i+1], list[i]
    return list
