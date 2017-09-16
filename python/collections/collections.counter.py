from collections import Counter

customers = int(input())

shoe_sizes = Counter(
    map(
        int,
        input().split()
    )
)

customer_number = int(input())

result = 0

for i in range(customer_number):
    c_size, c_money = map(
        int,
        input().split()
    )

    if shoe_sizes.get(c_size):
        result += c_money
        shoe_sizes[c_size] -= 1

print(result)
