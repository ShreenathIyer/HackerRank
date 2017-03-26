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