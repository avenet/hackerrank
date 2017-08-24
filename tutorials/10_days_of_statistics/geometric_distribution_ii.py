num, den = map(float, input().split())
inspections = int(input())

p = num / den
q = 1 - p

print(
    round(
        1 - ((1 - p) ** inspections),
        3
    )
)
