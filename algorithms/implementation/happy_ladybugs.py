from collections import defaultdict

q = int(input().strip())


def is_happy(board, index):
    item = board[index]
    
    prev_item_index = index - 1
    
    if 0 <= prev_item_index < len(board):
        if board[prev_item_index] == item:
            return True
    
    next_item_index = index + 1
    
    if 0 <= next_item_index < len(board):
        if board[next_item_index] == item:
            return True
    
    return False


def check_ladybugs_happy(board):
    for i in range(len(board)):
        if not is_happy(board, i):
            return False
    
    return True


def can_make_ladybugs_happy(board):
    board_item_counter = defaultdict(int)
    spaces = 0
    
    for c in board:
        if c != '_':
            board_item_counter[c] += 1
        else:
            spaces += 1
    
    if spaces == 0:
        return check_ladybugs_happy(board)
    else:
        for char, ocurrences in board_item_counter.items():
            if ocurrences == 1:
                return False
    
    return True


for a0 in range(q):
    n = int(input().strip())
    b = input().strip()
    
    if can_make_ladybugs_happy(b):
        print('YES')
    else:
        print('NO')
