#!/usr/bin/env python3
import time

def merge_lists(listA, listB):
    '''Merges two sorted lists into a new, sorted list.  The new list is sorted by percent, count, alpha.'''
    merged_list = []
    i = j = 0
    total = len(listA) + len(listB)
    time.sleep(1)
    while len(merged_list) != total:
        if len(listA) == i:
            merged_list += listB[j:]
            break
        elif len(listB) == j:
            merged_list += listA[i:]
            break
        elif listA[i].percent != listB[j].percent:
            if listA[i].percent > listB[j].percent:
                merged_list.append(listA[i])
                i += 1
            else:
                merged_list.append(listB[j])
                j += 1
        else:
            if listA[i].count != listB[j].count:
                if listA[i].count > listB[j].count:
                    merged_list.append(listA[i])
                    i += 1
                else:
                    merged_list.append(listB[j])
                    j += 1
            else:
                if listA[i].word > listB[j].word:
                    merged_list.append(listA[i])
                    i += 1
                else:
                    merged_list.append(listB[j])
                    j += 1

    return merged_list
