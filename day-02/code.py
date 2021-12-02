import fileinput
import re

lines = list(fileinput.input())

horizontal = 0
depth = 0
for line in lines:
    value = int(re.search(r'(\d+)', line).group(1))
    if 'forward' in line:
        horizontal += value
    elif 'up' in line:
        depth -= value
    elif 'down' in line:
        depth += value

print(depth*horizontal)

## part 2
horizontal = 0
depth = 0
aim = 0
for line in lines:
    value = int(re.search(r'(\d+)', line).group(1))
    if 'forward' in line:
        horizontal += value
        depth += aim * value
    elif 'up' in line:
        aim -= value
    elif 'down' in line:
        aim += value

print(depth*horizontal)