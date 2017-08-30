from math import erf, sqrt

mean, standard_deviation = map(int, input().split())

less_than = float(input())

begin, end = map(int, input().split())


def normal(x):
    return (1 + erf((x - mean) / (standard_deviation * sqrt(2)))) / 2

print(
    round(
        normal(less_than),
        3
    )
)

print(
    round(
        normal(end) - normal(begin),
        3
    )
)