def get_median(items):
    items_length = len(items)
    
    if items_length % 2 == 1:
        return items[int(items_length / 2)]
    
    upper_middle_pos = int(items_length / 2)
    lower_middle_pos = upper_middle_pos - 1
    
    return int(
        (items[upper_middle_pos] + items[lower_middle_pos]) / 2
    )


n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

print(
    get_median(
        list(numbers[0: int(n / 2)])
    )
)

if n % 2 == 1:
    print(
        numbers[int(n / 2)]
    )

    print(
        get_median(
            list(
                numbers[int(n / 2) + 1: n]
            )
        )
    )
else:
    print(
        get_median(numbers)
    )

    print(
        get_median(
            list(numbers[int(n / 2): n])
        )
    )
