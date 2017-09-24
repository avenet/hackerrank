cube = lambda x: x ** 3


def fibonacci(n):
    first, second = 0, 1

    for i in range(n):
        yield first
        first, second = second, first + second


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
