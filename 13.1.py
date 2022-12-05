array = []

with open('origami.txt') as f:
        dots = [ x.strip().split(',') for x in f.readlines()]
        
for x in dots:
    x[0] = int(x[0])
    x[1] = int(x[1])

for b in dots:
    if b[0] > 655:
        b[0] = 1310 - b[0]

for c in dots:
    if array.count(c) == 0:
        array.append(c)
      
print(len(array))