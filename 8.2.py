input = []
output = []
answer = 0

with open("input.txt", "r") as f:
    for row in f:
        line = row.strip().split(" | ")
        input.append(line[1:])
        output.append(line[:1])

squish_in = [ str(string) for large in input for string in large]
squish_out = [ str(string) for small in output for string in small]

stuff_in = [ sorted(a.split(), key=len) for a in squish_out]
stuff_out = [ b.split() for b in squish_in]

# just so you know: After sorting. 0 = 1, 1 = 7, 2 = 4, 9 = 8 => Always

z = 0
while z < len(stuff_in):
    dictionary = {
        ''.join(sorted(stuff_in[z][0])):1,
        ''.join(sorted(stuff_in[z][1])):7,
        ''.join(sorted(stuff_in[z][2])):4,
        ''.join(sorted(stuff_in[z][3])):0,
        ''.join(sorted(stuff_in[z][4])):0,
        ''.join(sorted(stuff_in[z][5])):0,
        ''.join(sorted(stuff_in[z][6])):0,
        ''.join(sorted(stuff_in[z][7])):0,
        ''.join(sorted(stuff_in[z][8])):0,
        ''.join(sorted(stuff_in[z][9])):8
        }

    for y in stuff_in[z]:
        temp3 = list(stuff_in[z][0])
        temp4 = list(stuff_in[z][2])
        if len(y) == 5:
            if all(letter in y for letter in temp3):
                l = {''.join(sorted(y)) : 3}
                dictionary.update(l)
            elif y.count(temp4[0])+y.count(temp4[1])+y.count(temp4[2])+y.count(temp4[3]) > 2 :
                m = {''.join(sorted(y)) : 5}
                dictionary.update(m)
            else:
                n = {''.join(sorted(y)) : 2}
                dictionary.update(n)
        elif len(y) == 6:
            if y.count(temp3[0])+y.count(temp3[1]) == 1:
                p = {''.join(sorted(y)) : 6}
                dictionary.update(p)
            elif all(letters in y for letters in temp4):
                q = {''.join(sorted(y)) : 9}
                dictionary.update(q)
    
    number = ""
    for x in stuff_out[z]:
        number += str(dictionary[''.join(sorted(x))])

    answer += int(number)
    z += 1
    
print(answer)