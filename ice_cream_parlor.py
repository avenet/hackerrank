cases = int(raw_input())

for case in xrange(cases):
    m = int(raw_input())
    n = int(raw_input())
    
    flavors = map(int, raw_input().split())
    
    found = False
    
    for i, a in enumerate(flavors):
        for j, b in enumerate(flavors):
            if i != j and a + b == m:
                print i+1, j+1
                found = True
                break
        if found:
            break