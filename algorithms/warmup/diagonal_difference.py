n = int(input())

r = 0
l = n - 1

right_diagonal = 0
left_diagonal = 0

for x in range(n):
    line = input()

    numbers = list(
        map(
            int,
            line.split()
        )
    )

    right_diagonal += numbers[r]
    left_diagonal += numbers[l]

    r += 1
    l -= 1

print(
    abs(
        right_diagonal - left_diagonal
    )
)