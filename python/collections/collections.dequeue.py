from collections import deque

cases = int(input())

d = deque()

for case in range(cases):
    console_input = input().split()
    
    if len(console_input) == 1:
        action = console_input[0]
        if action == 'pop':
            d.pop()
        elif action == 'popleft':
            d.popleft()
    elif len(console_input) == 2:
        action, item = console_input
        if action == 'append':
            d.append(item)
        elif action == 'appendleft':
            d.appendleft(item)

print(' '.join(d))
