import fileinput
from collections import Counter

inRaw = list(fileinput.input())
template = inRaw[0].rstrip()

rules = dict(l.rstrip().split(" -> ") for l in inRaw[2:])

for _ in range(10):
    polymer = ''
    for x in range(0, len(template)-1):
        polymer += template[x] + str(rules[template[x:x+2]])
    polymer += template[-1]
    template = polymer

counts = Counter(polymer)
print(max(counts.values()) - min(counts.values()))

#### Part 2 
windows = {}
for k, v in rules.items():
    windows[k] = (k[0]+v, v+k[1])

c = Counter()
for k in rules:
    c[k] = template.count(k)

count = Counter(template)
for _ in range(40):
    cc = c.copy()
    for k in cc:
        v = c[k]
        count[rules[k]] += v
        cc[k] -= v
        for key in windows[k]:
            cc[key] += v
    c = cc

print(max(count.values()) - min(count.values()))