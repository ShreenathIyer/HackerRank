import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, raw_input().strip().split(' ')))
b = list(map(int, raw_input().strip().split(' ')))

total = 0
flag = 0
flag1 = 0
max_one = max(a)
min_one = min(b)

for num in range(max_one, min_one + 1):
    for ele in b:
        if ele % num == 0:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        for ele2 in a:
            if num % ele2 == 0:
                continue
            else:
                flag1 = 1
                break
    if flag == 0 and flag1 == 0:
        total += 1
    flag = 0
    flag1 = 0

print total