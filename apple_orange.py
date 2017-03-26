#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

sum_apple = 0
sum_orange = 0

for fruit in apple:
    dist = a + fruit
    if dist >= s and dist <=t:
        sum_apple += 1

for fruit in orange:
    dist = b + fruit
    if dist >=s and dist <= t:
        sum_orange += 1

print sum_apple
print sum_orange
