with open('heatmap1.txt') as f:
    heatmap = [ [ int(val) for val in line ] for line in f.read().splitlines() ]

low = []

for x in range(len(heatmap)):
    for y in range(len(heatmap[x])):
        front, back, up, down = 0, 0, 0, 0
        if y == 0 and x == 0:
            front = heatmap[x][y+1]
            down = heatmap[x+1][y]
            if heatmap[x][y] < front and heatmap[x][y] < down:
                low.append(heatmap[x][y] + 1)
        elif y == len(heatmap[x]) - 1 and x == 0:
            back = heatmap[x][y-1]
            down = heatmap[x+1][y]
            if heatmap[x][y] < back and heatmap[x][y] < down:
                low.append(heatmap[x][y] + 1)
        elif y == 0 and x == len(heatmap) - 1:
            front = heatmap[x][y+1]
            up = heatmap[x-1][y]
            if heatmap[x][y] < front and heatmap[x][y] < up:
                low.append(heatmap[x][y] + 1)
        elif y == len(heatmap[x]) - 1 and x == len(heatmap) - 1:
            back = heatmap[x][y-1]
            up = heatmap[x-1][y]
            if heatmap[x][y] < back and heatmap[x][y] < up:
                low.append(heatmap[x][y] + 1)
        elif y == 0:
            front = heatmap[x][y+1]
            down = heatmap[x+1][y]
            up = heatmap[x-1][y]
            if heatmap[x][y] < front and heatmap[x][y] < down and heatmap[x][y] < up:
                low.append(heatmap[x][y] + 1)
        elif x == 0:
            front = heatmap[x][y+1]
            down = heatmap[x+1][y]
            back = heatmap[x][y-1]
            if heatmap[x][y] < front and heatmap[x][y] < down and heatmap[x][y] < back:
                low.append(heatmap[x][y] + 1)
        elif y == len(heatmap[x]) - 1:
            back = heatmap[x][y-1]
            down = heatmap[x+1][y]
            up = heatmap[x-1][y]
            if heatmap[x][y] < back and heatmap[x][y] < down and heatmap[x][y] < up:
                low.append(heatmap[x][y] + 1)
        elif x == len(heatmap) - 1:
            front = heatmap[x][y+1]
            up = heatmap[x-1][y]
            back = heatmap[x][y-1]
            if heatmap[x][y] < front and heatmap[x][y] < up and heatmap[x][y] < back:
                low.append(heatmap[x][y] + 1)
        else:
            front = heatmap[x][y+1]
            up = heatmap[x-1][y]
            back = heatmap[x][y-1]
            down = heatmap[x+1][y]
            if heatmap[x][y] < front and heatmap[x][y] < up and heatmap[x][y] < back and heatmap[x][y] < down:
                low.append(heatmap[x][y] + 1)

print(sum(low))



with open('heatmap1.txt') as f:
    heatmap = [ [ int(val) for val in line ] for line in f.read().splitlines() ]

class Heatmap:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def back(current):
        for a in points:
            if a.row == current.row and a.column == current.column - 1:
                return a

    def front(current):
        for b in points:
            if b.row == current.row and b.column == current.column + 1:
                return b

    def up(current):
        for c in points:
            if c.row == current.row - 1 and c.column == current.column:
                return c

    def down(current):
        for d in points:
            if d.row == current.row + 1 and d.column == current.column:
                return d

    def check(current):
        if (Heatmap.up(current) == None or current.value < (Heatmap.up(current)).value) \
        and (Heatmap.front(current) == None or current.value < (Heatmap.front(current)).value) \
        and (Heatmap.down(current) == None or current.value < (Heatmap.down(current)).value) \
        and (Heatmap.back(current) == None or current.value < (Heatmap.back(current)).value):
            return True


points = list()

for x in range(len(heatmap)):
    for y in range(len(heatmap[x])):
        points.append(Heatmap(x,y,heatmap[x][y]))

risk = 0

for x in points:
    if Heatmap.check(x) == True:
        risk += x.value + 1

print(risk)