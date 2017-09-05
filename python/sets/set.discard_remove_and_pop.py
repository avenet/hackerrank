n = int(input())
s = set(map(int, input().split()))
operation_count = int(input())

for operation_index in range(operation_count):
    command = input()
    command_parts = command.split()
    command_arg = None
    command_name = None
    
    if len(command_parts) == 1:
        command_name = command_parts[0]
    else:
        command_name, command_arg = command_parts
        command_arg = int(command_arg)
    
    if command_name == 'pop':
        s.pop()
    elif command_name == 'discard':
        s.discard(command_arg)
    elif command_name == 'remove':
        s.remove(command_arg)

print(sum(s))
