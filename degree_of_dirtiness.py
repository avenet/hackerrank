testcases = int(raw_input())

for testcase in xrange(testcases):
    n, m = map(int, raw_input().split())
    
    toilets = [0 for x in xrange(n)]
    
    top = n - 1
    bottom = 0
    i = 0
    assign_top = False
    
    while i < n:
        if assign_top:
            toilets[top] = (i + 1) % n
            top -= 1
        else:
            toilets[bottom] = (i + 1) % n
            bottom += 1
        assign_top = not assign_top
        i += 1
    
    rest = m % n
    division = m / n
    
    if not rest:
        division -= 1
    
    if n % 2 == 1 and m / n % 2 == 1 and rest != 0:
        if m % 2 == 0:
            rest += 1
        else:
            rest -= 1
    
    position = toilets.index(rest) + 1
    print '{0} {1}'.format(position, division)