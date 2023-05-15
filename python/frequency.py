import re
from collections import defaultdict
f = open('input', 'r')
total = []
while True:
    file_line = f.readline()
    if not file_line:
        break
    params = file_line.split(':')
    date = params[0]
    nums = params[1].strip()
    numbers_with_integer = [int(x) if x != '' else '0' for x in re.split(', | /', nums)]
    total += numbers_with_integer

frequency = defaultdict(int)

for numbers in total:
    frequency[numbers] += 1
print(sorted(frequency.items(), key=lambda x:x[1], reverse=True))
f.close()
