import sys

a0,a1,a2 = raw_input().strip().split(' ')
A = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
B = [int(b0),int(b1),int(b2)]

a = 0
b = 0

for i, j in zip(A, B):
    if i > j:
        a += 1
    elif i < j:
        b += 1

print a, b
