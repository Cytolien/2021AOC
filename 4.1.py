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

# boards = [[[22,13,17,11,0],
# [8,2,23,4,24],
# [21,9,14,16,7],
# [6,10,3,18,5],
# [1,12,20,15,19]],
# [[3,15,0,2,22],
# [9,18,13,17,5],
# [19,8,7,25,23],
# [20,11,10,24,4],
# [14,21,16,12,6]],
# [[14,21,17,24,4],
# [10,16,15,9,19],
# [18,8,23,26,20],
# [22,11,13,6,5],
# [2,0,12,3,7]]]

vertical = [[[0 for d in boards[0][0]] for e in boards[0]] for f in boards]

i = 0
while i < len(boards):
    j = 0
    while j < 5:
        k = 0
        while k < 5:
            vertical[i][j][k] = boards[i][k][j]
            k += 1
        j += 1
    i += 1

board_length = len(boards[0])
row_length = len(boards[0][0])

l = 0
while l < len(boards):
    m = 0
    while m < 5:
        boards[l].append(vertical[l][m])
        m += 1
    l += 1

#calls = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
calls = [26,55,7,40,56,34,58,90,60,83,37,36,9,27,42,19,46,18,49,52,75,17,70,41,12,78,15,64,50,54,2,77,76,10,43,79,22,32,47,0,72,30,21,82,6,95,13,59,16,89,1,85,57,62,81,38,29,80,8,67,20,53,69,25,23,61,86,71,68,98,35,31,4,33,91,74,14,28,65,24,97,88,3,39,11,93,66,44,45,96,92,51,63,84,73,99,94,87,5,48]

def checkCall():
    call = []
    for z in calls:
        call.append(z)

        for board_i in range(len(boards)):
            for row_i in range(len(boards[board_i])):
                if all(var in call for var in boards[board_i][row_i]):
                    return boards[board_i], call


winningBoard, calledNums = checkCall()
winningSum = sum(val for val in reduce(lambda x, y: x+y, winningBoard[:5]) if val not in calledNums) * calledNums[-1]

print(winningSum)