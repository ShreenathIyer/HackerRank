'''
Created on Jun 26, 2017

@author: Shreenath.Iyer
'''
v = int(input())
n = int(input())
ar = []
ar.append(map(int, raw_input().strip().split(' ')))
ar = ar[0]
print ar.index(v)