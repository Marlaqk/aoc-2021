import fileinput

empty = set()
eastFacing = set()
southFacing = set()

lines = [l.rstrip() for l in list(fileinput.input())]
height = len(lines)
width = len(lines[0])

for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == '.':
            empty.add((x,y))
        elif lines[x][y] == 'v':
            southFacing.add((x,y))
        else:
            eastFacing.add((x,y))

def printGrid(empty, east, south, width, height):
    for x in range(height):
        line = ''
        for y in range(width):
            if (x,y) in empty:
                line += '.'
            elif (x,y) in east:
                line += '>'
            elif (x,y) in south:
                line += 'v'
        print(line)

step = 0
while True:
    doneMove = 0
    step += 1
    newEastFacing = set()
    addEmpty = set()
    removeEmpty = set()
    for x,y in eastFacing:
        newY = y + 1 if y < width - 1 else 0
        if (x,newY) in empty:
            doneMove = 1
            addEmpty.add((x,y))
            removeEmpty.add((x,newY))
            newEastFacing.add((x,newY))
        else:
            newEastFacing.add((x,y))

    empty.difference_update(removeEmpty)
    empty.update(addEmpty)
    eastFacing = newEastFacing
    addEmpty = set()
    removeEmpty = set()
    newSouthFacing = set()
    for x,y in southFacing:
        newX = x + 1 if x < height - 1 else 0
        if (newX,y) in empty:
            doneMove = 1
            addEmpty.add((x,y))
            removeEmpty.add((newX,y))
            newSouthFacing.add((newX,y))
        else:
            newSouthFacing.add((x,y))
    # add free spots
    empty.difference_update(removeEmpty)
    empty.update(addEmpty)
    southFacing = newSouthFacing
    if not doneMove:
        print(step)
        break