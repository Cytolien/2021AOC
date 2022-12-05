with open("crab.txt") as f:
    for row in f:
        line = row.strip().split(",")
    crabs = [ int(x) for x in line]

min_fuel = 10000000

i = 0
while i < max(crabs):
    fuel = 0
    for x in crabs:
        fuel += abs(x - i)
    
    if fuel < min_fuel:
        min_fuel = fuel

    i += 1

print(min_fuel)