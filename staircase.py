#!/bin/python

n = int(raw_input().strip())
for i in range(1, n):
    print (n - int(i) - 1) * ' ',
    print i * '#'
print n * '#'