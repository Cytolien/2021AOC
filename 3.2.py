with open('binary.txt') as f:   
    diag = [ val.strip() for val in f.readlines() ]

#diag = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

summed = [ sum(int(row[z]) for row in [list(x) for x in diag]) for z in range(len([list(x) for x in diag][0])) ]

if summed[0] >= len(diag)/2:
        oxygen = [x for x in diag if x[0] == '1']
        carbon = [x for x in diag if x[0] == '0']

i = 1
while i < len(oxygen[0]):
    summed_oxy = [ sum(int(row[z]) for row in [list(x) for x in oxygen]) for z in range(len([list(x) for x in oxygen][0])) ]
    if len(oxygen) == 1:
        break
    else:
        if summed_oxy[i] >= len(oxygen)/2:
            oxygen = [x for x in oxygen if x[i] == '1']
        else:
            oxygen = [x for x in oxygen if x[i] == '0']
    i += 1

j = 1
while j < len(carbon[0]):
    summed_car = [ sum(int(row[z]) for row in [list(x) for x in carbon]) for z in range(len([list(x) for x in carbon][0])) ]
    if len(carbon) == 1:
        break
    else:
        if summed_car[j] >= len(carbon)/2:
            carbon = [x for x in carbon if x[j] == '0']
        else:
            carbon = [x for x in carbon if x[j] == '1']
    j += 1

print(int(oxygen[0], 2)*int(carbon[0], 2))