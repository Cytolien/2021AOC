class Heatmap:
    def __init__(self, row, column, value, mark):
        self.row = row
        self.column = column
        self.value = value
        self.mark = mark

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
        setup = [Heatmap.up(current), Heatmap.front(current), Heatmap.down(current), Heatmap.back(current)]
        around = [n for n in setup if n]
        conclusion = [True if ((y.mark == True or current.value < y.value) and current.value != 9) else False for y in around] 
        if any(conclusion):
            return True
            
def basincheck(f):
    counter = 0
    if Heatmap.up(f) != None and (Heatmap.up(f)).mark == False and Heatmap.check(Heatmap.up(f)) == True:
        counter += 1
        Heatmap.up(f).mark = True
        counter += basincheck(Heatmap.up(f))
    
    if Heatmap.front(f) != None and (Heatmap.front(f)).mark == False and Heatmap.check(Heatmap.front(f)) == True:
        counter += 1
        Heatmap.front(f).mark = True
        counter += basincheck(Heatmap.front(f))
  
    if Heatmap.down(f) != None and (Heatmap.down(f)).mark == False and Heatmap.check(Heatmap.down(f)) == True:
        counter += 1
        Heatmap.down(f).mark = True
        counter += basincheck(Heatmap.down(f))

    if Heatmap.back(f) != None and (Heatmap.back(f)).mark == False and Heatmap.check(Heatmap.back(f)) == True:
        counter += 1
        Heatmap.back(f).mark = True
        counter += basincheck(Heatmap.back(f))
    return counter

with open('heatmap.txt') as f:
    heatmap = [ [ int(val) for val in line ] for line in f.read().splitlines() ]

points = list()
for x in range(len(heatmap)):
    for y in range(len(heatmap[x])):
        points.append(Heatmap(x,y,heatmap[x][y], False))

risk = []
for x in points:
    basin = 0
    if Heatmap.check(x) == True:
        basin += 1
        x.mark = True
        basin += basincheck(x)
        risk.append(basin)

risk.sort(reverse=True)
print(risk[0]*risk[1]*risk[2])