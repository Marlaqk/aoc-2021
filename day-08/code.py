import fileinput
from collections import defaultdict
import re

lines = list(map(str.rstrip, fileinput.input()))

# part 1
counts = defaultdict(int)
for line in lines:
    outputs = list(line.split(' | ')[1].split(' '))
    for x in outputs:
        counts[len(x)] += 1

print(sum(counts[x] for x in [2,3,4,7]))

# part 2
DECODE = {
    (6, 2, 3): "0",
    (2, 2, 2): "1",
    (5, 1, 2): "2",
    (5, 2, 3): "3",
    (4, 2, 4): "4",
    (5, 1, 3): "5",
    (6, 1, 3): "6",
    (3, 2, 2): "7",
    (7, 2, 4): "8",
    (6, 2, 4): "9",
}

def decode():
    for line in lines:
        numbers = re.findall("[a-g]+", line)
        one, _, four, *_ = sorted(numbers[:-4], key=len)
        one = set(one)
        four = set(four)

        yield "".join(
            DECODE[
                len(digit),
                len(one.intersection(digit)),
                len(four.intersection(digit)),
            ]
            for digit in numbers[-4:]
        )

print(sum(map(int, decode())))