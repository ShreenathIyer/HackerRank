'''
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a0, a1, a2), and the rating for Bob's challenge to be the triplet B = (b0, b1, b2).

Your task is to find their comparison points by comparing a0 with b0, a1 with b1, and a2 with b2.

If ai > bi, then Alice is awarded 1 point.
If ai < bi, then Bob is awarded 1 point.
If ai = bi, then neither person receives a point.
Comparison points is the total points a person earned.

Given A and B, can you compare the two challenges and print their respective comparison points?

Input Format:

The first line contains 3 space-separated integers, a0, a1, and a2, describing the respective values in triplet A. 
The second line contains 3 space-separated integers, b0, b1, and b2, describing the respective values in triplet B.

Constraints:

1 <= ai <= 100
1 <= bi <= 100

Output Format:

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

Sample Input:

5 6 7
3 6 10

Sample Output:

1 1 

'''
#!/bin/python

import sys

a0,a1,a2 = raw_input().strip().split(' ')
A = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
B = [int(b0),int(b1),int(b2)]

a = 0
b = 0

for i, j in zip(A, B):
    if i > j:
        a += 1
    elif i < j:
        b += 1

print a, b
