import fileinput

lines = list(fileinput.input())

gamma = ""
for x in range(0, len(lines[0])-1):
    countOnes = 0
    for y in range(0,len(lines)):
        if lines[y][x] == "1":
            countOnes += 1
    if countOnes >= len(lines)/2:
        gamma += "1"
    else:
        gamma += "0"

epsilon = gamma.translate(str.maketrans("01","10"))
print(int(gamma,2) * int(epsilon, 2))

# Part 2
def getLeadingNum(lines, idx):
    count = 0
    for line in lines:
        if line[idx] == '1':
            count += 1
    return '1' if count >= len(lines)/2 else '0'

oxygenRating = 0
filteredItems = lines
comperator = gamma[0]
for x in range(len(gamma)):
    filteredItems = list(filter(lambda el: el[x] == comperator, filteredItems))
    if len(filteredItems) == 1:
        oxygenRating = int(filteredItems[0], 2)
        break
    comperator = getLeadingNum(filteredItems, x+1)

co2Rating = 0
filteredItems = lines
comperator = gamma[0]
for x in range(len(gamma)):
    filteredItems = list(filter(lambda el: el[x] != comperator, filteredItems))
    if len(filteredItems) == 1:
        co2Rating = int(filteredItems[0], 2)
        break
    comperator = getLeadingNum(filteredItems, x+1)

print(oxygenRating*co2Rating)