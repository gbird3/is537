import difflib
# arr = [1, 2, 5, 6, 7]

# for i in len(100):
#     if arr(i) != i + 1
#         print(i)

arr = []
arrCorrect = []
# def findMissing():
for i in range(100):
    if i != 6:
        arr.append(i)

for i in range(100):
    arrCorrect.append(i)

correctString = "".join(str(x) for x in arrCorrect)
string = "".join(str(x) for x in arr)

diff = difflib.unified_diff(string, correctString)

diff = ''.join(diff)

print(diff)

# half the array
