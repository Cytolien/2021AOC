with open('depth.txt') as f:   
    list = [ int(val.strip()) for val in f.readlines() ]

var = 0
input = list[0]

for x in list:
    if x > input:
        var += 1
    input = x
print(var)


print(sum(1 if list[i] < list[i+1] else 0 for i in range(len(list) - 1)))