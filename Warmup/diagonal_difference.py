'''
Given a square matrix of size N * N, calculate the absolute difference between the sums of its diagonals.

Input Format:

The first line contains a single integer, N. The next N lines denote the matrix's rows, with each line containing N space-separated integers describing the columns.

Constraints:

-100 <= Elements in the matrix <= 100

Output Format:

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input:

3
11 2 4
4 5 6
10 8 -12

Sample Output:

15
'''
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
