def partition(arr, low, high):
    '''
    Partition sorts the section of the list that is passed in using
    the high as the pivot and the low as the starting number
    '''
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high],arr[i+1]

    return ( i+1 )

def quick_sort(list, low, high):
    '''
    A python implementation of quick sort. Quick sort calls partition
    to sort then takes the two sections and calls quick sort again
    '''
    if low < high:

        part = partition(list, low, high)

        quick_sort(list, low, part - 1)
        quick_sort(list, part + 1, high)
