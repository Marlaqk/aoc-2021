import fileinput
from collections import defaultdict
import re

grid = [list(map(int, line.strip())) for line in fileinput.input()]
riskValue = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        up = grid[x-1][y] if x > 0 else 10
        down = grid[x+1][y] if x < len(grid)-1 else 10
        right = grid[x][y + 1] if y < len(grid[x]) -1 else 10
        left = grid[x][y - 1] if y > 0 else 10
        p = grid[x][y]
        if up > p and down > p and left > p and right > p:
            riskValue += p + 1

print(riskValue)

def fill(x, y, v):
    if grid[x][y] == 9:
        return 0
    if basins[x][y] >= 0:
        return 0
    basins[x][y] = v
    result = 1
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]):
            result += fill(nx, ny, v)
    return result

basins = [[-1] * len(grid[0]) for _ in range(len(grid))]
basin = 0
sizes = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        size = fill(x, y, basin)
        if size:
            sizes.append(size)
            basin += 1
sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])