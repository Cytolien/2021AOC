with open("fish.txt") as f:
    for row in f:
        line = row.strip().split(",")
    fish = [ int(x) for x in line]

days = 80
newfish = 8

i = 0
while i < days:
    for x in range(len(fish)):
        fish[x] -= 1
        if fish[x] < 0:
            fish.append(newfish)
            fish[x] = 6
    i += 1

print(len(fish))