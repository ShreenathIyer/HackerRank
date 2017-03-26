#!/bin/python

import sys
import string

h = map(int,raw_input().strip().split(' '))
word = raw_input().strip()

max_ht = 1

for charac in word:
    ind = string.lowercase.index(charac)
    curr_ht = h[ind]
    if max_ht < curr_ht:
        max_ht = curr_ht

area = len(word) * max_ht
print area