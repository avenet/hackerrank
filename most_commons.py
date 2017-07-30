str_input = raw_input()

ocurrences_dict = {}

for char in str_input:
    if char not in ocurrences_dict:
        ocurrences_dict[char] = 1
    else:
        ocurrences_dict[char] += 1
        
characters = list(ocurrences_dict)

def compare(x, y):
    comparison = cmp(ocurrences_dict[x], ocurrences_dict[y])
    
    if comparison:
        return comparison
    
    return cmp(y, x)

characters.sort(cmp=compare)

for c in characters[-1:-4:-1]:
    print '%s %s' % (c, ocurrences_dict[c])