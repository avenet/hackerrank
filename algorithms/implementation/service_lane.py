n, t = list(
    map(
        int,
        input().split()
    )
)

lanes = list(map(int, input().split()))

for testcase in range(t):
    ini, end = list(
        map(
            int,
            input().split()
        )
    )

    min_width = min(lanes[ini: end+1])
    print(min_width)
