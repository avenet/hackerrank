testcases = int(raw_input())

for testcase in xrange(testcases):
    n = int(raw_input())
    numbers = [0 for _ in xrange(n)]
    
    top = n
    bottom = 1
    i = n - 1
    
    put_top = True
    
    while i >= 0:
        if put_top:
            numbers[i] = str(top)
            top -= 1
        else:
            numbers[i] = str(bottom)
            bottom += 1
        i-=1
        put_top = not put_top
        
    print ' '.join(numbers)
