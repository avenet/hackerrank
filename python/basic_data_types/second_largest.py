if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    largest = -101
    second_largest = -102

    for item in arr:
        if item > largest:
            largest, second_largest = item, largest
        elif item > second_largest and item != largest:
            second_largest = item
    
    print(second_largest)
