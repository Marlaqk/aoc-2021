import fileinput
from collections import Counter
from itertools import chain

lines = list(fileinput.input())
queue = list(map(int,lines.pop(0).split(',')))

boardsIn = [] 
board = []
lc = 0
for line in lines[1:]:
    if line == '\n':
        board = []
        lc = 0
        continue
    board.append([(int(x), False) for x in line.split(' ') if x != ''])
    lc += 1
    if lc == 5:
        boardsIn.append(board)

def checkBoards(boards):
    for idx, board in enumerate(boards):
        for row in board:
            if Counter(el[1] for el in row).get(True) == len(row):
                return sum(nr for nr, state in list(chain.from_iterable(board)) if state == False), idx
        for col in zip(*board):
            if Counter(el[1] for el in col).get(True) == len(col):
                return sum(nr for nr, state in list(chain.from_iterable(board)) if state == False), idx
    return 0, 0

## part 1
boards = boardsIn
for number in queue:
    for y in range(len(boards)):
        for x in range(len(boards[y])):
            boards[y][x] = [(nr, True) if nr == number else (nr, state) for nr, state in boards[y][x]]
    val, idx = checkBoards(boards)
    if val > 0:
        print(val * number)
        break

## part 2
boards = boardsIn
for idxNumber, number in enumerate(queue):
    val, idx = checkBoards(boards)
    while val > 0:
        boards.pop(idx)
        print(len(boards))
        if len(boards) == 0:
            print(val * queue[idxNumber-1])
        val, idx = checkBoards(boards)
    for y in range(len(boards)):
        for x in range(len(boards[y])):
            boards[y][x] = [(nr, True) if nr == number else (nr, state) for nr, state in boards[y][x]]