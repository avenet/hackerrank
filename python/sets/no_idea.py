n, m = map(int, input().split())

items = list(map(int, input().split()))
set_a = list(map(int, input().split()))
set_b = list(map(int, input().split()))

happiness_level = 0

for item in items:
    in_a = item in set_a
    in_b = item in set_b

    if in_a and not in_b:
        happiness_level += 1
    elif in_b and not in_a:
        happiness_level -= 1

print(happiness_level)