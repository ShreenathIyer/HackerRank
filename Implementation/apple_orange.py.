#!/bin/python

'''
Input Format:

The first line contains two space-separated integers denoting the respective values of s and t. 
The second line contains two space-separated integers denoting the respective values of a and b. 
The third line contains two space-separated integers denoting the respective values of m and n. 
The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point a. 
The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point b.

Constraints:

1 <= s,t,a,b,m,n <= 10^5
-10^5 <= d <= 10^5
a < s < t < b

Output Format:

Print two lines of output:

1) On the first line, print the number of apples that fall on Sam's house.
2) On the second line, print the number of oranges that fall on Sam's house.

Sample Input 0:

7 11
5 15
3 2
-2 2 1
5 -6

Sample Output 0:

1
1
'''

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
