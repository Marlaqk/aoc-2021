import fileinput
from collections import defaultdict
import re

lines = list(fileinput.input())

points = defaultdict(int)
for line in lines:
    x1,y1,x2,y2 = map(int, re.findall(r'\d+', line))
    
    for offset in range(max(abs(x1 - x2), abs(y1 - y2))+1):
        signX = 0 if x1 == x2 else 1 if x1 < x2 else -1;
        signY = 0 if y1 == y2 else 1 if y1 < y2 else -1;
        points[(x1 + offset * signX, y1 + offset * signY)] += 1

print(sum(val >= 2 for key, val in points.items()))