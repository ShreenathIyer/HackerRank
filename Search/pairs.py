'''
Given N integers, count the number of pairs of integers whose difference is K.

Input Format:

The first line contains N and K. 
The second line contains N numbers of the set. All the N numbers are unique.

Constraints:

2 <= N <= 10^5
0 < K < 10^9
Each integer will be greater than  and at least  smaller than .

Output Format:

An integer that tells the number of pairs of integers whose difference is K.

Sample Input:

5 2  
1 5 3 4 2  

Sample Output:

3
'''
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = list(map(int, raw_input().strip().split(' ')))
i = 0
j = 1
count = 0

a = sorted(a)

while j < n:
    diff = a[j] - a[i]
    if diff == k:
        count += 1
        j += 1
    elif diff > k:
        i += 1
    elif diff < k:
        j += 1

print count
