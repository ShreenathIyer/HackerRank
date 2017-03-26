# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input().strip().split(' ')
n = int(n[0])
a = list(map(int, raw_input().strip().split(' ')))
m = raw_input().strip().split(' ')
m = int(m[0])
b = list(map(int, raw_input().strip().split(' ')))
'''
c = {number: [occurence_in_a, occurence_in_b],

     number: [occurence_in_a, occurence_in_b],

     number: [occurence_in_a, occurence_in_b], ...}
'''
c = {}

for num in b:
    if num not in c:
        c[num] = [0, 1]
    else:
        c[num][1] += 1

for num in a:
    if num not in c:
        c[num] = [1, 0]
    else:
        c[num][0] += 1

missing = []

for number in c:
    if c[number][0] < c[number][1]:
        missing.append(number)

missing = sorted(missing)

for each in missing:
    print each,