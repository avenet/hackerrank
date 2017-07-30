cases = int(raw_input())

def get_numbers(size, a, b):
    current_level = set([0])
    
    for _ in xrange(size-1):
        next_level = set()
        for item in current_level:
            next_level.add(item+a)
            next_level.add(item+b)
            
        current_level = next_level
        
    return sorted(current_level)
    
    

for case in xrange(cases):
    n, a, b = int(raw_input()), int(raw_input()), int(raw_input())
    
    print ' '.join(map(str, get_numbers(n, a, b)))
