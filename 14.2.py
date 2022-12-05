with open('chemicals1.txt') as o:
    elements = [ x.strip().split(' -> ') for x in o.readlines()]

def exponential(base, num):
    compounds = []
    another = []
    var = ''
    cat = ''
    num -= 1
    
    for a in base:
        var = var + a
        if len(var) == 2:
            compounds.append(var)
            var = var[1:]
            
    for b in range(len(compounds)):
        for z in elements:
            print(compounds[b], z[0], num)
            if compounds[b] == z[0] and num != 0:
                another.append(compounds[b][:1] + z[1])
                print(another)
                
    for something in another:
        print(something, num)
        exponential(something, num)
        return another

original = 'NNCB'
polymer = exponential(original, 2)

print(polymer)

# element = set(polymer)
# most, least = polymer.count(next(iter(element))), polymer.count(next(iter(element)))

# for w in element:
#     print(w, polymer.count(w))
#     if polymer.count(w) > most:
#         most = polymer.count(w)
#     if polymer.count(w) < least:
#         least = polymer.count(w)

# print(most - least)

# test original: NNCB
# puzzle input: SNVVKOBFKOPBFFFCPBSF