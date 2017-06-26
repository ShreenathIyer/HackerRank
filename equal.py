'''
Created on Mar 28, 2017

@author: Shreenath.Iyer
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