import sys

n = int(raw_input().strip())
arr = map(float, raw_input().strip().split(' '))

neg = 0.0
pos = 0.0
zer = 0.0

for num in arr:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zer += 1

print("%6f" %(pos / len(arr)))
print("%6f" %(neg / len(arr)))
print("%6f" %(zer / len(arr)))