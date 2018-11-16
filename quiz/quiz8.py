# 1-800-COM-PUTE => 1-800-7883
# 1-801-BYU.INFO => 1801.298.4636

str = '1801BYUINFO'
print(str[:4])

str = str[4:]
num = ''

for i in str:
    # check if is numeric, if so add number to string.
    # else calculate number
    if i == 'A' or i == 'B' or i == 'C':
        print(1)
    elif i == 'D' or i == 'E' or i == 'F':
        print(2)
    elif i == 'D' or i == 'E' or i == 'F':
        print(3)
    elif i == 'G' or i == 'H' or i == 'I':
        print(4)
    elif i == 'J' or i == 'K' or i == 'L':
        print(5)
    elif i == 'M' or i == 'N' or i == 'O':
        print(6)
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        print(7)
    elif i == 'T' or i == 'U' or i == 'V':
        print(8)
    else:
        print(9)
