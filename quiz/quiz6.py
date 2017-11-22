a = 0
b = 1
number = 10

i = 0

print(a)
print(b)

for i in range(number):
    num = a+b

    a = b
    b = num

    print(num)
