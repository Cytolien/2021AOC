class Octopus():
    def __init__(self, row, col, val, mark):
        self.row = row
        self.col = col
        self.val = val
        self.mark = mark

    def __str__(self):
         return f'{self.val}'

    def back(current):
        for a in octopi:
            if a.row == current.row and a.col == current.col - 1:
                return a
    
    def front(current):
        for b in octopi:
            if b.row == current.row and b.col == current.col + 1:
                return b
    
    def up(current):
        for c in octopi:
            if c.row == current.row - 1 and c.col == current.col:
                return c
    
    def down(current):
        for d in octopi:
            if d.row == current.row + 1 and d.col == current.col:
                return d

    def upback(current):
        for e in octopi:
            if e.row == current.row - 1 and e.col == current.col - 1:
                return e

    def upfront(current):
        for f in octopi:
            if f.row == current.row - 1 and f.col == current.col + 1:
                return f

    def downfront(current):
        for g in octopi:
            if g.row == current.row + 1 and g.col == current.col + 1:
                return g

    def downback(current):
        for h in octopi:
            if h.row == current.row + 1 and h.col == current.col - 1:
                return h

    def checkAdjacent(current):
        setup = (Octopus.up(current), Octopus.front(current), Octopus.down(current), Octopus.back(current), \
                Octopus.upback(current), Octopus.upfront(current), Octopus.downfront(current), Octopus.downback(current))

        around = (n for n in setup if n)
        for p in around:
            p.val += 1
            if p.val > 9 and p.mark != True:
                p.mark = True
                Octopus.checkAdjacent(p)


def reset():
    for octo in octopi:
        octo.mark = False
        if octo.val > 9:
            octo.val = 0
    

with open('flash.txt') as f:
    info = [[int(x) for x in line] for line in f.read().strip().splitlines()]

octopi = list()
for row in range(len(info)):
    for col in range(len(info[row])):
        octopi.append(Octopus(row, col, info[row][col], False))

steps = 1000
for z in range(1,steps):
    for octopus in octopi:
        octopus.val += 1
        if octopus.val > 9 and octopus.mark != True:
            octopus.mark = True
            Octopus.checkAdjacent(octopus)

    if all(octopus.mark == True for octopus in octopi):
        print(z)
        break
    reset()

print()