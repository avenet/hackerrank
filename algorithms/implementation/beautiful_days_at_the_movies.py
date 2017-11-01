i, j, k = map(int, input().split())

result = 0


def is_beautiful(number, factor):
    reversed_number = int(str(number)[::-1])
    return abs(number - reversed_number) % factor == 0


for current_number in range(i, j + 1):
    if is_beautiful(current_number, k):
        result += 1

print(result)
