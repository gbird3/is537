from array_api import Array
import csv

filename = 'data.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        print('{}:{},{},{}'.format(i, row[0], row[1], row[2]))
        if row[0] == 'CREATE':
            array1 = Array()
        elif row[0] == 'ADD':
            array1.add(row[1])
        elif row[0] == 'DEBUG':
            array1.debug_print()
        elif row[0] == 'SET':
            array1.set(int(row[1]), row[2])
        elif row[0] == 'GET':
            array1.get(int(row[1]))
        elif row[0] == 'DELETE':
            array1.delete(int(row[1]))
        elif row[0] == 'INSERT':
            array1.insert(int(row[1]), row[2])
        elif row[0] == 'SWAP':
            array1.swap(int(row[1]), int(row[2]))
        else:
            print('This shouldn\'t be there')
        i += 1
