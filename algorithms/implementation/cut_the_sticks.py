def make_cut(l):
    smallest = min(l)

    return [
        x - smallest
        for x
        in l
        if x - smallest > 0
    ]


length = int(input())

current = list(
    map(
        int,
        input().split()
    )
)

while current:
    print(len(current))
    current = make_cut(current)
