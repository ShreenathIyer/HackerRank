'''
Created on Jun 7, 2017

@author: Shreenath.Iyer
'''
v = map(int, raw_input().strip().split(' '))
v = v[0]
n = map(int, raw_input().strip().split(' '))
n = n[0]
ar = []
ar.append(map(int, raw_input().strip().split(' ')))
ar = ar[0]

if n % 2 == 0:
    mid = (n / 2)
else:
    mid = (n / 2) + 1
start = 0
end = n - 1

while ar[mid] != v:
    if v < ar[mid]:
        end = mid - 1
        n = end - start
        if n % 2 == 0:
            mid = (n / 2)
        else:
            mid = (n / 2) + 1
    else:
        start = mid + 1
        n = start - end
        if n % 2 == 0:
            mid = (n / 2)
        else:
            mid = (n / 2) + 1

print mid