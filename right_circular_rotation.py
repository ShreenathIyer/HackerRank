import sys
from collections import deque

n, k, q = raw_input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = map(int, raw_input().strip().split(' '))

items = deque(a)
items.rotate(k)

for a0 in xrange(q):
    m = int(raw_input().strip())
    print items[m]