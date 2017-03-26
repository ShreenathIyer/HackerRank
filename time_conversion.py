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