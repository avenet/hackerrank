def spiral_iterator():
    x, y = 0, 0
    
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    i = 1
    print x,y
    
    while True:
        dir_index = (i - 1) % 4
        vector = i * direction[dir_index][0], i * direction[dir_index][1]
        x += vector[0]
        y += vector[1]
        print x,y
        i += 1
        raw_input()

result = spiral_iterator()