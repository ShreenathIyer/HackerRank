def array_left_rotation(a, n, k):
    temp = list(a)
    for i in range(0, len(a)):
        diff = i - k
        if diff < 0:
            diff = len(a) + diff
        temp[diff] = a[i]
    return temp


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
