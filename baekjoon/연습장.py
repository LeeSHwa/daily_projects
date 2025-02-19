import sys


k = 10

count = [x for x in range(k)]

print(count)

for i in range(len(count)):
    sys.stdout.readline(print(count[i]))
    