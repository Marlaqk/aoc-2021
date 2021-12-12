import fileinput
from collections import defaultdict

paths = []
nodes = defaultdict(list)

def findPath(path, node, choosenNode):
    if node == 'end':
        path.append(node)
        paths.append(','.join(path))
        return
    
    path.append(node)
    for n in nodes[node]:
        if n.islower() and n in path:
            if choosenNode is None:
                findPath(path[:], n, n)
            else:
                continue
        else:
            findPath(path[:], n, choosenNode)

lines = list(fileinput.input())
for line in lines:
    f,t = line.rstrip().split('-')
    nodes[f].append(t)
    if f != 'start':
        nodes[t].append(f)

findPath([], 'start', None)
print(len(paths))