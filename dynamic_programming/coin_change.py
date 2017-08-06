#!/bin/python3
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = list(map(int, input().strip().split(' ')))
total_coins = len(coins)
coins.sort()


def memoize(f):
    cache = {}

    def decorated(n, i):
        if cache.get((n, i)):
            return cache[(n, i)]

        result = f(n, i)
        cache[(n, i)] = result
        return result

    return decorated


@memoize
def get_ways(n, start_index):
    if n == 0:
        return 1

    result = 0

    for i in range(start_index, total_coins):
        if n >= coins[i]:
            result += get_ways(n - coins[i], i)

    return result


print(get_ways(n, 0))
