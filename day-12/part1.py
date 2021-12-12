import fileinput
from collections import defaultdict

paths = []
nodes = defaultdict(list)

def findPath(path, node):
    if node == 'end':
        path.append(node)
        paths.append(','.join(path))
        return
    
    path.append(node)
    for n in nodes[node]:
        if n.islower() and n in path:
            continue
        findPath(path[:], n)

lines = list(fileinput.input())
for line in lines:
    f,t = line.rstrip().split('-')
    nodes[f].append(t)
    if f != 'start':
        nodes[t].append(f)

findPath([], 'start')
print(len(paths))