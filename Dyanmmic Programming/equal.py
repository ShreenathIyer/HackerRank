'''
Created on Mar 28, 2017

@author: Shreenath.Iyer

Problem: 
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and may have distributed the chocolates unequally. One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.

But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,

For every operation, she can choose one of her colleagues and can do one of the three things.

1. She can give one chocolate to every colleague other than chosen one.
2. She can give two chocolates to every colleague other than chosen one.
3. She can give five chocolates to every colleague other than chosen one.
Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates. 

Input Format:

First line contains an integer T denoting the number of testcases. T testcases follow. 
Each testcase has 2 lines. First line of each testcase contains an integer N denoting the number of colleagues. Second line contains N space separated integers denoting the current number of chocolates each colleague has.

Constraints:

1 <= T <= 100
1 <= N <= 10000

Number of initial chocolates each colleague has < 1000 

Output Format:

T lines, each containing the minimum number of operations needed to make sure all colleagues have the same number of chocolates.

Sample Input

1
4
2 2 3 7
Sample Output

2

'''
#from math import ceil, floor

def equality(chocs, mini):
    count = 0
    for each in chocs:
        if each - mini >= 5:
            count += (each - mini) // 5
            each = mini + (each - mini) % 5
        if each - mini >= 2:
            count += (each - mini) // 2
            each = mini + (each - mini) % 2
        if each - mini == 1:
            count += 1
    return count
                
if __name__ == "__main__":
    t = int(input())
    n = []
    chocs = []
    for i in range(0, t):
        temp_n = int(input())
        n.append(temp_n)
        temp_chocs = list(map(int,raw_input().strip().split(' ')))
        chocs.append(temp_chocs)
        
    for i in range(0, len(n)):
        chocs[i] = sorted(chocs[i])
        mini = chocs[i][0]
        final = [equality(chocs[i], mini)]
        final.append(equality(chocs[i], mini - 2))
        final.append(equality(chocs[i], mini - 1))
        print(min(final))
