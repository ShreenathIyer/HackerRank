'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Input Format:

A single string containing a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM), where 01 <= hh <= 12 and 00 <= mm, ss <= 59.

Output Format:

Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

Sample Input:

07:05:45PM

Sample Output:

19:05:45

'''

import sys

time = raw_input().strip().split(':')
# for curr in range(len(time), 0, -1):
ss, fmt = int(time[len(time) - 1][:len(time[len(time) - 1])/2]), time[len(time) - 1][len(time[len(time) - 1])/2:]
hh, mm = int(time[0]), int(time[1])

if fmt == 'AM' and hh == 12:
    hh = 0
elif fmt == 'PM' and hh != 12:
    hh += 12

sys.stdout.write("%02d" % (hh))
sys.stdout.write(':')
sys.stdout.write("%02d" % (mm))
sys.stdout.write(':')
sys.stdout.write("%02d" % (ss))
