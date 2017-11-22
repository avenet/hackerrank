n, k = map(int, input().split())
numbers = map(int,input().split())

remainder_counts = [0] * k

for number in numbers:
    remainder_counts[number % k] += 1

result = min(remainder_counts[0], 1)

for i in range(1, k//2 + 1):
    if i != k - i:
        result += max(
            remainder_counts[i],
            remainder_counts[k-i]
        )

if k % 2 == 0:
    result += 1

print(result)
