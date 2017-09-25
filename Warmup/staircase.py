'''
Consider a staircase of size n =4:

   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.

Input Format:

A single integer, n, denoting the size of the staircase.

Output Format:

Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input:

6 

Sample Output:

     #
    ##
   ###
  ####
 #####
######
'''

#!/bin/python

n = int(raw_input().strip())
for i in range(1, n):
    print (n - int(i) - 1) * ' ',
    print i * '#'
print n * '#'
