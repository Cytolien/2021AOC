import matplotlib.pyplot as plt

with open('origami.txt') as o:
        dots = [ x.strip().split(',') for x in o.readlines()]
        
with open('folds.txt') as f:
        folding = [ x.strip().split('=') for x in f.readlines()]
        
for x in dots:
    x[0] = int(x[0])
    x[1] = int(x[1])

for y in folding:
    y[1] = int(y[1])

for z in folding:
    for a in dots:
        if z[0] == 'x':
            if a[0] > z[1]:
                a[0] = (z[1] * 2) - a[0]
        elif z[0] == 'y':
            if a[1] > z[1]:
                a[1] = (z[1] * 2) - a[1]

array = []
for c in dots:
    if array.count(c) == 0:
        array.append(c)

for node in array:
    plt.scatter(node[0], node[1])
    
plt.xticks([l for l in range(41)])
plt.yticks([m for m in range(1)])

plt.show()

#result was inverted... needed to add a y=-10 at the end of folds.txt