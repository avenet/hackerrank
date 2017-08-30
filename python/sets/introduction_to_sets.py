def average(array):
    numbers = set(array)
    return round(
        sum(numbers) / float(
            len(numbers)
        ),
        3
    )

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
