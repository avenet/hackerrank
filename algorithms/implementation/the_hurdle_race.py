n, k = input().strip().split(' ')
n, k = [int(n), int(k)]

hurdle_heights = list(
    map(
        int,
        input().strip().split(' ')
    )
)

max_height = max(hurdle_heights)

beverages_to_drink = 0

if max_height > k:
    beverages_to_drink = max_height - k

print(beverages_to_drink)
