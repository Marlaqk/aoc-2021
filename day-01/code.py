import fileinput

lines = list(map(int,list(fileinput.input())))

def part1():
    return sum([1 for idx, val in enumerate(lines[1:]) if val > lines[idx]])

def part2():
    slidingWindows = [sum(lines[i:i+3]) for i in range(0, len(lines)-2)]
    return sum([1 for idx, val in enumerate(slidingWindows[1:]) if val > slidingWindows[idx]])

print(part1())
print(part2())