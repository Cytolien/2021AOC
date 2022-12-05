with open('NavSub.txt') as f:
    navigation = [ [char for char in line] for line in f.read().splitlines() ]

begin = [[] for h in navigation]
end = [[] for i in navigation]
count = 0

def pair(a,b):
    if a == '(' and b == ')' or a == '{' and b == '}' or a == '[' and b == ']' or a == '<' and b == '>': 
        return True
    else:
        return False

for x in range(len(navigation)):
    for y in range(len(navigation[x])):
        if y+1 != len(navigation[x]):
            if navigation[x][y] == '(' or navigation[x][y] == '[' or navigation[x][y] == '{' or navigation[x][y] == '<':
                begin[x].append(navigation[x][y])
            else:
                end[x].append(navigation[x][y])         
                if pair(begin[x][-1], end[x][0]):
                    end[x].pop(0)
                    begin[x].pop(-1)
                else:
                    break
        else:
            break

for z in range(len(end)):
    if len(end[z]) > 0:
        if end[z][0] == ')':
            count += 3
        elif end[z][0] == ']':
            count += 57
        elif end[z][0] == '}':
            count += 1197
        elif end[z][0] == '>':
            count += 25137
    
print(count)