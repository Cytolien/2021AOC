import math
with open('NavSub.txt') as f:
    navigation = [ [char for char in line] for line in f.read().splitlines() ]

begin = [[] for h in navigation]
end = [[] for i in navigation]
incomplete = [[] for j in navigation ]

def pair(a,b):
    if a == '(' and b == ')' or a == '{' and b == '}' or a == '[' and b == ']' or a == '<' and b == '>': 
        return True
    else:
        return False

def complete(c):
    if c == '(':
        return(')')
    elif c == '{':
        return('}')
    elif c == '[':
        return(']')
    elif c == '<':
        return('>')

for x in range(len(navigation)):
    for y in range(len(navigation[x])):
        if navigation[x][y] == '(' or navigation[x][y] == '[' or navigation[x][y] == '{' or navigation[x][y] == '<':
            begin[x].append(navigation[x][y])
        else:
            end[x].append(navigation[x][y])         
            if pair(begin[x][-1], end[x][0]):
                end[x].pop(0)
                begin[x].pop(-1)
            else:
                begin[x] = ['']
                break
    begin[x].reverse()
    if begin[x] != '':
        for z in begin[x]:
            incomplete[x].append(complete(z))

count = []

for p in range(len(incomplete)):
    counter = 0
    for q in range(len(incomplete[p])):
        counter *= 5
        if incomplete[p][q] == ')':
            counter += 1
        elif incomplete[p][q] == ']':
            counter += 2
        elif incomplete[p][q] == '}':
            counter += 3
        elif incomplete[p][q] == '>':
            counter += 4
    if counter != 0:
        count.append(counter)

count.sort()
print(count[math.ceil(len(count)/2) - 1])