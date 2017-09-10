set_a = set(
    map(int, input().split())
)

set_count = int(input())

result = True

for _ in range(set_count):
    current_set = set(
        map(int, input().split())
    )
    
    if not set_a >= current_set:
        result = False
        break

print(result)
