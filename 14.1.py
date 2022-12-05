with open('chemicals.txt') as o:
    elements = [ x.strip().split(' -> ') for x in o.readlines()]

def exponential(base):
    compounds = []
    another = []
    var = ''
    cat = ''
    
    for a in base:
        var = var + a
        if len(var) == 2:
            compounds.append(var)
            var = var[1:]
            
    for b in range(len(compounds)):
        for z in elements:
            if compounds[b] == z[0] and b != len(compounds) - 1:
                another.append(compounds[b][:1] + z[1])
            elif compounds[b] == z[0]:
                another.append(compounds[b][:1] + z[1]+ compounds[b][1:])

    for y in another:
        cat = cat + y
    
    return cat

# test original: NNCB
# puzzle input: SNVVKOBFKOPBFFFCPBSF

original = 'SNVVKOBFKOPBFFFCPBSF'
polymer = exponential(original)
    
for christmas in range(9):
    polymer = exponential(polymer)

element = set(polymer)
most, least = polymer.count(next(iter(element))), polymer.count(next(iter(element)))

for w in element:
    print(w, polymer.count(w))
    if polymer.count(w) > most:
        most = polymer.count(w)
    if polymer.count(w) < least:
        least = polymer.count(w)
        
print(most - least)