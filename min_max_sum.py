#!/bin/python
import sys

a, b, c, d, e = raw_input().strip().split(' ')
unsorted_list = [int(a), int(b), int(c), int(d), int(e)]

min = unsorted_list[0]
max = unsorted_list[len(unsorted_list) - 1]
sum = 0

for num in unsorted_list:
    if num <= min:
        min = num
    if num >= max:
        max = num
    sum += num

print sum - max,
print sum - min
