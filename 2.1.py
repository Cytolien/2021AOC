from re import findall as r_find

with open('direction.txt') as f:   
    list = [ val.strip() for val in f.readlines() ]

horizontal = 0
vertical = 0

for x in list:
    num = next(int(val) for val in r_find('[0-9]+', x))
    if x.startswith('f'):
        horizontal += num
    if x.startswith('u'):
        vertical -= num
    if x.startswith('d'):
        vertical += num
        
print(horizontal*vertical)