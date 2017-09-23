n, items = int(input()), input().split()
print(any(map(lambda x: x == x[::-1], items)) and all(map(lambda x: int(x) >= 0, items)))
