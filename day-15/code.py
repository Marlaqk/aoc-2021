
import fileinput
from collections import defaultdict
from queue import PriorityQueue
import math
import operator
from itertools import product

grid = defaultdict(int)
lines = [l.rstrip() for l in list(fileinput.input())]
for x in range(len(lines)):
    for y in range(len(lines[x])):
        grid[(x,y)] = int(lines[x][y])

def tupleAdd(a, b):
    return tuple(map(operator.add,a,b))

def tupleSub(a,b):
    return tuple(map(operator.sub,a,b))

def manhatten(a):
    return sum(abs(x) for x in a)

def find_shortest_path(grid, start, end):
    steps = PriorityQueue()
    steps.put((0, start))
    g_score = defaultdict(lambda: math.inf, {start: 0})

    while steps:
        _, current = steps.get()
        if current == end:
            return g_score[current]
        for neighbor in [tupleAdd(current, d) for d in [(0,-1),(-1,0),(1,0),(0,1)] if grid[tupleAdd(current, d)] > 0]:
            tentative_g_score = g_score[current] + grid[neighbor]
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhatten(tupleSub(neighbor,end))
                steps.put((f_score, neighbor))

# part 2
big_grid = defaultdict(int)
lx = len(lines)
ly = len(lines[0])
for (x, y), v in grid.items():
    for a, b in product(range(5), repeat=2):
        nv = (v + a + b) % 9
        big_grid[(x + a * lx, y + b * ly)] = 9 if nv == 0 else nv

print(find_shortest_path(grid, (0,0), max(grid)))
print(find_shortest_path(big_grid, (0,0), max(big_grid)))