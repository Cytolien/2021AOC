with open('depth.txt') as f:   
    list = [ int(val.strip()) for val in f.readlines() ]

var = 0
input = list[0]+list[1]+list[2]
tri = []

for x in list:
    tri.append(x)
    if len(tri) == 3:
        value = sum(tri)
        if value > input:
            var += 1
        input = value
        tri.pop(0)
print(var)

print(sum(1 if sum(list[i:i+3]) < sum(list[i+1:i+4]) else 0 for i in range(len(list) - 3)))