a = [1, 4, 6, 9]
b = [2, 3, 4, 5, 6, 8, 10]

a_pos = 0
b_pos = 0
c = []

while a_pos < len(a) and b_pos < len(b):
    if a[a_pos] < b[b_pos]:
        c.append(a[a_pos])
        a_pos += 1
    else:
        c.append(b[b_pos])
        b_pos += 1

# Not part of my solution
while a_pos < len(a):
    c.append(a[a_pos])
    a_pos +=1

while b_pos < len(b):
    c.append(b[b_pos])
    b_pos +=1


print(c)
