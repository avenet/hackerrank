n = int(raw_input())
cavity_map = []

def get_value(cavity_map, i, j):
    return int(cavity_map[i][j])

def is_cavity(cavity_map, i, j):
    number = get_value(cavity_map, i, j)
    a1 = get_value(cavity_map, i, j + 1)
    a2 = get_value(cavity_map, i, j - 1)
    a3 = get_value(cavity_map, i + 1, j)
    a4 = get_value(cavity_map, i - 1, j)
    
    return number > a1 and number > a2 and number > a3 and number > a4

for i in xrange(n):
    cavity_map.append([x for x in raw_input()])

for i in xrange(n):
    line_result = ''
    for j in xrange(n):
        if i != 0 and i != n-1 and j != 0 and j != n-1:
            if is_cavity(cavity_map, i, j):
                line_result += 'X'
                continue
        line_result += cavity_map[i][j]
    print line_result