n = int(input())

result = set(map(int, input().split()))

operations = int(input())

for _ in range(operations):
    operation = input().split()[0]
    target_set = set(map(int, input().split()))
    
    if operation == 'update':
        result.update(target_set)
    elif operation == 'intersection_update':
        result.intersection_update(target_set)
    elif operation == 'difference_update':
        result.difference_update(target_set)
    elif operation == 'symmetric_difference_update':
        result.symmetric_difference_update(target_set)

print(sum(result))
