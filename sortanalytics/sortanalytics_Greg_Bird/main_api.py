#!/usr/bin/env python3
import time

from bubblesort_api import bubble_sort
from insertionsort_api import insertion_sort
from selectionsort_api import selection_sort
from quicksort_api import quick_sort

FILENAMES = [
    [ 'list1.txt', 'int'   ],
    [ 'list2.txt', 'int'   ],
    [ 'list3.txt', 'int'   ],
    [ 'list4.txt', 'int'   ],
    [ 'list5.txt', 'float' ],
    [ 'list6.txt', 'int'   ],
]


class Result:
    def __init__(self, name, duration, nums):
        self.name = name
        self.duration = duration
        self.nums = nums
        self.relative = None

def print_results(list_name, results):
    print(list_name)
    for result in results:
        print(result.name)
        print(result.duration)
        print('{}%'.format(result.relative))
        print('First 10: {}'.format(', '.join([ str(item) for item in result.nums[:10] ])))
        print('Last 10: {}'.format(', '.join([ str(item) for item in result.nums[-10:] ])))
        print()


def determine_fastest(results):
    fastest = results[0].duration
    for i in range(len(results) - 1):
        if fastest > results[i].duration:
            fastest = results[i].duration

    return fastest

def calculate_relative(results, fastest):
    for result in results:
        result.relative = round(100.0 * (result.duration - fastest) / fastest)
    return results


def main():
    for i in FILENAMES:
        results = []
        with open(i[0], 'r') as file:
            list_name = i[0]
            text = file.read()
            numbers = text.split()
            if i[1] == 'int':
                numbers = [ int(x) for x in numbers ]
            elif i[1] == 'float':
                numbers = [ float(x) for x in numbers ]

            # Native sort
            one_thousand = []
            for i in range(1000):
                one_thousand.append(numbers[:])

            start = time.time()
            for i in one_thousand:
                i.sort()
            duration = round(time.time() - start, 6)
            results.append(Result('Native Language Sort', duration, i))

            # Bubble sort
            one_thousand = []
            for i in range(1000):
                one_thousand.append(numbers[:])

            start = time.time()
            for i in one_thousand:
                sorted_numbers = bubble_sort(i)
            duration = round(time.time() - start, 6)

            results.append(Result('Bubble Sort', duration, sorted_numbers))

            # Insertion sort
            one_thousand = []
            for i in range(1000):
                one_thousand.append(numbers[:])

            start = time.time()
            for i in one_thousand:
                sorted_numbers = insertion_sort(i)
            duration = round(time.time() - start, 6)

            results.append(Result('Insertion Sort', duration, sorted_numbers))

            # Selection sort
            one_thousand = []
            for i in range(1000):
                one_thousand.append(numbers[:])

            start = time.time()
            for i in one_thousand:
                sorted_numbers = selection_sort(i)
            duration = round(time.time() - start, 6)
            results.append(Result('Selection Sort', duration, sorted_numbers))

            # Quick sort
            one_thousand = []
            for i in range(1000):
                one_thousand.append(numbers[:])

            start = time.time()
            for i in one_thousand:
                quick_sort(i, 0, len(i) - 1)
            duration = round(time.time() - start, 6)
            results.append(Result('Quick Sort', duration, i))

            fastest = determine_fastest(results)
            calculate_relative(results, fastest)

            results.sort(key=lambda x: x.relative)
            print_results(list_name, results)


### Main runner ###
if __name__ == '__main__':
    main()
