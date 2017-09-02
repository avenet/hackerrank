n, m = map(int, input().split())
items = list(map(int, input().split()))
happiness_dict = {}

for item in map(int, input().split()):
    happiness_dict[item] = 1

for item in map(int, input().split()):
    happiness_dict[item] = -1

happiness_level = 0

for item in items:
    happiness_level += happiness_dict.get(item, 0)

print(happiness_level)