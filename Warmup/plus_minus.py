'''
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Input Format:

The first line contains an integer, N, denoting the size of the array. 
The second line contains N space-separated integers describing an array of numbers (a0, a1, a1, ..., an-1).

Output Format:

You must print the following 3 lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.

Sample Input:

6
-4 3 -9 0 4 1         

Sample Output:

0.500000
0.333333
0.166667
'''
import sys

n = int(raw_input().strip())
arr = map(float, raw_input().strip().split(' '))

neg = 0.0
pos = 0.0
zer = 0.0

for num in arr:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zer += 1

print("%6f" %(pos / len(arr)))
print("%6f" %(neg / len(arr)))
print("%6f" %(zer / len(arr)))
