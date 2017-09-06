m = int(input())

english_newspaper_subscriptors = set(
    map(
        int,
        input().split()
    )
)

n = int(input())

french_newspaper_subscriptors = set(
    map(
        int,
        input().split()
    )
)

print(
    len(
        english_newspaper_subscriptors | french_newspaper_subscriptors
    )
)
