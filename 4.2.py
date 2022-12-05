from re import findall as re_findall
from functools import reduce

with open('Bingo.txt', 'r') as a:
    boards = [[]]
    cur_board = boards[0]
    for b in a:
        if not b.strip():
            boards.append([])
            cur_board = boards[-1]
            continue
        
        cur_board.append([int(val) for val in re_findall('[0-9]+', b.strip())])

vertical = [[[0 for d in boards[0][0]] for e in boards[0]] for f in boards]

i = 0
while i < len(boards):
    j = 0
    while j < len(boards[0]):
        k = 0
        while k < len(boards[0][0]):
            vertical[i][j][k] = boards[i][k][j]
            k += 1
        j += 1
    i += 1

l = 0
while l < len(boards):
    m = 0
    while m < 5:
        boards[l].append(vertical[l][m])
        m += 1
    l += 1

calls = [26,55,7,40,56,34,58,90,60,83,37,36,9,27,42,19,46,18,49,52,75,17,70,41,12,78,15,64,50,54,2,77,76,10,43,79,22,32,47,0,72,30,21,82,6,95,13,59,16,89,1,85,57,62,81,38,29,80,8,67,20,53,69,25,23,61,86,71,68,98,35,31,4,33,91,74,14,28,65,24,97,88,3,39,11,93,66,44,45,96,92,51,63,84,73,99,94,87,5,48]
boards_to_remove = []

def checkCall():
    call = []
    for z in calls:
        call.append(z)
        for board_i in range(len(boards)):
            for row_i in range(len(boards[board_i])):
                if boards[board_i] not in boards_to_remove:
                    if all(var in call for var in boards[board_i][row_i]):
                        if len(boards)-1 == len(boards_to_remove):
                            return boards_to_remove, call
                        else:
                            boards_to_remove.append(boards[board_i])
                     
def losingBoard(x):
    for w in range(len(boards)):
        if boards[w] not in x:
            return boards[w]

winningBoards, calledNums = checkCall()
loser = losingBoard(winningBoards)
winningSum = sum(val for val in reduce(lambda x, y: x+y, loser[:5]) if val not in calledNums) * calledNums[-1]
print(winningSum)