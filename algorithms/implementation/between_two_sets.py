def get_numbers_between(set_a, set_b):
    numbers_between = 0

    for candidate in range(1, 101):
        found = True

        for item in set_a:
            if candidate % item:
                found = False
                break

        if not found:
            continue

        for item in set_b:
            if item % candidate:
                found = False
                break

        if found:
            numbers_between += 1

    return numbers_between


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = get_numbers_between(a, b)
    print(total)
