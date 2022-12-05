from re import findall as r_find

with open('direction.txt') as f:   
    list = [ val.strip() for val in f.readlines() ]

horizontal = 0
vertical = 0
aim = 0

for x in list:
    num = next(int(val) for val in r_find('[0-9]+', x))
    if x.startswith('f'):
        horizontal += num
        vertical += aim * num
    if x.startswith('u'):
        aim -= num
    if x.startswith('d'):
        aim += num
        
print(horizontal*vertical)