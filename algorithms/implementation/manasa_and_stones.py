cases = int(input())


def get_numbers(size, a, b):
    current_level = {0}
    
    for _ in range(size - 1):
        next_level = set()
        for item in current_level:
            next_level.add(item + a)
            next_level.add(item + b)
        
        current_level = next_level
    
    return sorted(current_level)


for case in range(cases):
    n, a, b = int(input()), int(input()), int(input())

    print(' '.join(map(str, get_numbers(n, a, b))))
