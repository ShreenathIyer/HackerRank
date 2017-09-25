'''
Consider two sets of positive integers, A = {a0, a1, ..., an-1} and B = {b0, b1, ..., bn-1}. We say that a positive integer,x , is between sets A and B if the following conditions are satisfied:

1) All elements in A are factors of x.
2) x is a factor of all elements in B.
Given A and B, find and print the number of integers (i.e., possible x's) that are between the two sets.

Input Format:

The first line contains two space-separated integers describing the respective values of  (the number of elements in set A) and  (the number of elements in set B). 
The second line contains n distinct space-separated integers describing a0, a1, ..., an-1. 
The third line contains m distinct space-separated integers describing b0, b1, ..., bn-1.

Constrains:
1 <= n,m <= 100
1 <= ai <= 100
1 <= bi <= 100

Output Format:

Print the number of integers that are considered to be between A and B.

Sample Input:

2 3
2 4
16 32 96

Sample Output:

3

'''

import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, raw_input().strip().split(' ')))
b = list(map(int, raw_input().strip().split(' ')))

total = 0
flag = 0
flag1 = 0
max_one = max(a)
min_one = min(b)

for num in range(max_one, min_one + 1):
    for ele in b:
        if ele % num == 0:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        for ele2 in a:
            if num % ele2 == 0:
                continue
            else:
                flag1 = 1
                break
    if flag == 0 and flag1 == 0:
        total += 1
    flag = 0
    flag1 = 0

print total
