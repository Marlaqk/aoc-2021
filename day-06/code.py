import fileinput
from collections import defaultdict
import re

def calc(fish, days):
    nrFishes = defaultdict(int)
    for f in fish:
        nrFishes[f] += 1

    for _ in range(days):
        spawnNr = nrFishes[0]
        for x in range(1,9):
            nrFishes[x-1] = nrFishes[x]
        nrFishes[8] = spawnNr
        nrFishes[6] += spawnNr

    return sum(x for x in nrFishes.values())


fish = list(map(int, re.findall(r'\d+', list(fileinput.input())[0])))

# part 1
print(calc(fish, 80))
# part 2
print(calc(fish, 256))