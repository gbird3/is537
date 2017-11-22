def selection_sort(list):
    '''
    A python implementation of selection sort
    '''

    for i in range(len(list)):
        min_number = i
        for j in range(i+1, len(list)):
            if list[min_number] > list[j]:
                min_number = j

        list[i], list[min_number] = list[min_number], list[i]

    return list
