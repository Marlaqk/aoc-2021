
import fileinput
import numpy as np

grid = np.array([list(map(int, x.strip())) for x in fileinput.input()])
grid = np.pad(grid.astype('float'), 1, constant_values=np.nan)

def needFlash(grid):
    return set(map(tuple, np.argwhere(grid == 10)))

def step(grid):
    count = 0
    gr = grid + 1
    todo = needFlash(gr)
    while todo:
        count += 1
        y, x = todo.pop()
        gr[y-1:y+2,x-1:x+2] += 1
        todo |= needFlash(gr)
    gr[gr > 9] = 0
    return gr, count

def part1(grid):
    flashes = 0
    for _ in range(100):
        grid, count = step(grid)
        flashes += count
    return flashes

def part2(grid):
    i = 0
    w, h = grid.shape
    n = (w - 2) * (h - 2)
    while True:
        i += 1
        grid, count = step(grid)
        if count == n:
            return i

print(part1(grid))
print(part2(grid))