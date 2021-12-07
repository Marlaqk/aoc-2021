import fileinput
import re

crabsPos = list(map(int, re.findall(r'\d+', list(fileinput.input())[0])))

# part 1
fuelCost = []
for x in range(max(crabsPos)):
    fuelCost.append(sum(abs(x - y) for y in crabsPos))
    if fuelCost[x] > fuelCost[x - 1]:
        print(fuelCost[x - 1])
        break

# part 2
fuelCost = []
for x in range(max(crabsPos)):
    fuelCost.append(sum(sum(range(abs(x - y)+1)) for y in crabsPos))
    if fuelCost[x] > fuelCost[x - 1]:
        print(fuelCost[x - 1])
        break