coords = []
with open('Steam.txt') as f:
    for row in f:
        line = row.strip().split(' -> ')
        for first_coor in line:
            first = first_coor.split(',')
            if first[0] not in coords and first[1] not in coords:
                coords.append([int(first[0]), int(first[1])])

lines = [[] for x in coords]

i = 0
while i < (len(coords) - 1):
    x1 = coords[i][0]
    y1 = coords[i][1]
    x2 = coords[i+1][0]
    y2 = coords[i+1][1]
    if x1 == x2:                
        if y1 > y2:
            for leo in reversed(range(y2, y1+1)):
                lines[i].append([x1,leo])
        else:
            for raph in range(y1, y2+1):
                lines[i].append([x1,raph])
        i += 2
    elif y1 == y2:
        if x1 > x2:
            for mich in reversed(range(x2, x1+1)):
                lines[i].append([mich, y1])
        else:
            for don in range(x1, x2+1):
                lines[i].append([don, y1])
        i += 2
    else:           
        i += 2

clean = [ var for var in lines if var != []]

duplicates = []

squish = [ val for xy in clean for val in xy ]
for x in squish:
    if squish.count(x) > 1:
        if x not in duplicates:
            duplicates.append(x)

print(len(duplicates))






# class Line(object):
#     def __init__(self, first_point, last_point):
#         first_point = first_point
#         self.last_point = last_point

# class Coord(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "% s, % s" %(self.x,self.y)

# if __name__ == '__main__':
    
    #for coord in coords:
    #    counter = 0
    #    while counter < 2:
    #        lines.append(Line(coord.point))

                #first_points.append(Coord(first))
                #for num in first:
                #    int(num)
                #    print(num)