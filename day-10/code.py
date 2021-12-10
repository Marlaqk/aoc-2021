import fileinput

def reverse(stack):
    new_stack = []
    while len(stack):
        new_stack.append(stack.pop())
    return new_stack

lines = list(map(str.rstrip, fileinput.input()))
penalty = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
score = 0
incomplete = []
for line in lines:
    stack = []
    invalid = 0
    for x in line:
        if x in brackets.keys():
            stack.append(brackets[x])
        else:
            if x != stack.pop():
                score += penalty[x]
                invalid = 1
                break
    if not invalid:
        incomplete.append(reverse(stack))

# part 1 
print(score)

# part 2
penalty = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
scores = []
for inc in incomplete:
    score = 0
    for x in inc:
        score = score * 5 + penalty[x]
    scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])