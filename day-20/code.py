from collections import defaultdict
import fileinput

inRaw = list(fileinput.input())
template = inRaw[0].rstrip()

image = defaultdict(int)
imageLines = [x.strip() for x in inRaw[2:]]

for x in range(len(imageLines)):
    for y in range(len(imageLines[x])):
        if imageLines[x][y] == '#':
            image[(x,y)] = 1

def getPixel(x,y, image):
    b = ''
    for xi in range(x-1,x+2):
        for yi in range(y-1,y+2):
            b += '1' if (xi,yi) in image else '0'
    if template[int(b, base=2)] == '#':
        return 1
    return 0


maxX, maxY = tuple(map(max, *image.keys()))
minX, minY = tuple(map(min, *image.keys()))
minX -= 200
maxX += 200
minY -= 200
maxY += 200

for _ in range(50):
    newImage = defaultdict(int)
    for px in range(minX - 1, maxX+1):
        for py in range(minY - 1, maxY+1):
            if getPixel(px,py, image):
                newImage[(px,py)] = 1
    image = newImage.copy()
    minX += 3
    maxX -= 3
    minY += 3
    maxY -= 3

print(len(image))