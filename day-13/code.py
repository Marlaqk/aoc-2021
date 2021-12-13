import fileinput
from collections import defaultdict
import re

def fold(dots, dir, cord):
    new_dots = defaultdict(int)
    for x,y in dots:
        if dir == 'x' and x > cord:
            x = 2 * cord - x
        if dir == 'y' and y > cord:
            y = 2 * cord - y
        new_dots[(x,y)] += 1

    return new_dots

dots = defaultdict(int)
idx = 0
lines = list(fileinput.input())
while 1:
    if lines[idx] == '\n':
        break
    p1, p2 = map(int, re.findall(r'\d+', lines[idx]))
    dots[(p1,p2)] += 1
    idx += 1

for line in lines[idx+1:]:
    direction,cord = re.findall(r'[x,y]=\d+', line)[0].split('=')
    dots = fold(dots, direction, int(cord))

# print activation key
for y in range(6):
    for x in range(40):
        if (x, y) in dots:
            print("##", end="")
        else:
            print("..", end="")
    print()
