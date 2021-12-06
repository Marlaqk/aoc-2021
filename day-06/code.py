import fileinput
from collections import defaultdict
import re

fish = list(map(int, re.findall(r'\d+', list(fileinput.input())[0])))

# part 1
for day in range(80):
    for x in range(len(fish)):
        if fish[x] == 0:
            fish[x] = 6
            fish.append(8)
        else:
            fish[x] -= 1

print(len(fish))

# part 2
nrFishes = defaultdict(int)
for f in fish:
    nrFishes[f] += 1

for day in range(80, 256):
    spawnNr = nrFishes[0]
    for x in range(1,9):
        nrFishes[x-1] = nrFishes[x]
    nrFishes[8] = spawnNr
    nrFishes[6] += spawnNr

print(sum(x for x in nrFishes.values()))