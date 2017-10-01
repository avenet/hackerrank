#!/bin/python3

DIRECTIONS = {
    'n': (0, -1),
    's': (0, 1),
    'e': (1, 0),
    'w': (-1, 0),
}


def get_route(preferred_direction):
    x_pos, y_pos = preferred_direction
    
    return [
        preferred_direction,
        (y_pos, x_pos),
        (-y_pos, -x_pos),
        (-x_pos, -y_pos)
    ]


class Board(object):
    def __init__(self, size):
        self._array = [
            [0] * size
            for _
            in range(size)
        ]
        self._size = size
    
    def is_in_range(self, x_pos, y_pos):
        return 0 <= x_pos < self._size and 0 <= y_pos < self._size
    
    def is_visited(self, x_pos, y_pos):
        return self.is_in_range(
            x_pos,
            y_pos
        ) and self._array[y_pos][x_pos]
    
    def set_value(self, x_pos, y_pos, value):
        self._array[y_pos][x_pos] = value
    
    def __str__(self):
        result = []
        
        for board_rows in self._array:
            result.append(' '.join(map(str, board_rows)))
        
        return '\n'.join(result)


if __name__ == "__main__":
    n = int(input().strip())
    d = input().strip()
    x, y = input().strip().split(' ')
    x, y = [int(x), int(y)]
    x, y = y, x
    
    current_value = 1
    
    board = Board(n)
    board.set_value(x, y, current_value)
    
    wind_direction = DIRECTIONS.get(d)
    
    direction_route = get_route(wind_direction)
    
    total_steps = n ** 2
    
    while current_value < total_steps:
        current_value += 1
        
        for direction in direction_route:
            new_x, new_y = x + direction[0], y + direction[1]
            
            if board.is_in_range(new_x, new_y) and not board.is_visited(new_x, new_y):
                board.set_value(new_x, new_y, current_value)
                x, y = new_x, new_y
                break
    
    print(board)
