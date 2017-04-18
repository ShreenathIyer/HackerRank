'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints:

Each integer is in the inclusive range [1, 10^9].

Output Format:

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
'''

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
