'''Reverse the words in string eg. 'The Sky is Blue'. then print 'Blue is Sky The'.'''

inp = raw_input().strip()
temp = inp.split(' ')
temp2 = []
for each in temp:
    temp2.insert(0, each)
print ' '.join(temp2)