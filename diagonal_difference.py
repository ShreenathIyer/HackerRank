#!/bin/python

import sys

n = int(raw_input().strip())
a = []
diag_one = 0
diag_two = 0

for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    diag_one = a_temp[a_i] + diag_one
    diag_two = a_temp[n - a_i - 1] + diag_two
    a.append(a_temp)

print abs(diag_one - diag_two)