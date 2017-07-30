cases = int(raw_input())

def compute_position(n):
    if not n:
        return 0, 0
    if n == 1:
        return 1, 0
    elif n == 2:
        return 1, 2
    
    rest = n % 4
    div = n / 4
    
    if not rest:
        return 2*-div, 2*-div
    elif rest == 1:
        return 2 * div + 1, 2*-div
    elif rest == 2:
        return 2 * div + 1, 2*div + 2
    
    return -(2*div + 2), 2*div + 2 
    

for case in xrange(cases):
    n = int(raw_input())
    x, y = compute_position(n)
    print '%s %s' % (x, y)