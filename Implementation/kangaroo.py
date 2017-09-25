'''
There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). 
The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump. 
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump. 
Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?

Input Format:

A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.

Constraints:

0 <= x1 <= x2 <= 10000
1 <= v1 <= 10000
1 <= v2 <= 10000

Output Format:

Print YES if they can land on the same location at the same time; otherwise, print NO.

Note: The two kangaroos must land at the same location after making the same number of jumps.

Sample Input 0:

0 3 4 2

Sample Output 0:

YES
'''
#!/bin/python

import sys

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if ((x2 > x1) and (v2 > v1)):
    print 'NO'    
else:
    if ((v1 != v2) and ((x2 - x1) % (v1 - v2)) == 0):
        print 'YES'
    else:
        print 'NO'
