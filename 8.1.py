output = []
count = 0

with open("input.txt", "r") as f:
    for row in f:
        line = row.strip().split(" | ")
        output.append(line[1:])

squish = [ str(string) for small in output for string in small]

stuff = [ a.split() for a in squish]

z = 0
while z < len(stuff):
    for x in stuff[z]:
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            count += 1
    z += 1
print(count)