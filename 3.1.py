with open('binary.txt') as f:   
    diag = [ val.strip() for val in f.readlines() ]

gamma_list = [0,0,0,0,0,0,0,0,0,0,0,0]
for x in diag:
    j = 0
    while j < len(x):
        if x[j] == '1':
            gamma_list[j] += 1
        j += 1

gamma = ''.join(['1' if z > (len(diag)/2) else '0' for z in gamma_list])
i = 0
epsilon = ''
while i < len(gamma):
    if gamma[i]=='1':
        epsilon += '0'
    else:
        epsilon += '1'
    i += 1

print(int(epsilon, 2)*int(gamma, 2)) 