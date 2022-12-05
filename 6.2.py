with open("fish.txt") as f:
    for row in f:
        line = row.strip().split(",")
    fish = [ int(x) for x in line]

days = 256
zero,one,two,three,four,five,six,seven,eight = fish.count(0), fish.count(1), fish.count(2), fish.count(3), fish.count(4), fish.count(5), fish.count(6), fish.count(7), fish.count(8)

i = 0
while i < days:
    zero, one, two, three, four, five, six, seven, eight = one, two, three, four, five, six, seven+zero, eight, zero
    i+=1
print(zero+one+two+three+four+five+six+seven+eight)

#fishes = list(map(fish.count, range(9)))

#for _ in range(256):
    #tmp = fishes[1:]
    #tmp.append(fishes[0])
    #tmp[6] += fishes[0]
    #fishes = tmp[:]

#for i in range(256):
#    fishes[(i+7) % 9] += fishes[i % 9]

#print(sum(fishes))

