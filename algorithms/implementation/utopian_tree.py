cases = int(input())

for case in range(cases):
    cycles = int(input())
    spring = True
    height = 1
    
    for cycle in range(cycles):
        if spring:
            height *= 2
        else:
            height += 1

        spring = not spring

    print(height)
