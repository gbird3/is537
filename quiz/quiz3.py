foo = [1, 2, [3, [4, 5]], 6]

# use recursion to print out the first one and then all the arrays below

def print_foo(arr):

    print(arr)

    # if not the last one in the array, go into the next array and print
    print_foo()
