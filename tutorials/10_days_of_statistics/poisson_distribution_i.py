from functools import reduce
from operator import mul

E = 2.71828


def poisson_distribution(t, k):
    success_probability = t ** k
    distribution_part = 1.0 / (E ** t)
    successes_combination = fact(k)
    
    return (
        (
            success_probability * distribution_part
        ) / successes_combination
    )


def fact(number):
    if number == 0:
        return 1
    
    return reduce(
        mul,
        range(1, number + 1)
    )


mean = float(input())
random_variable_value = int(input())

print(
    round(
        poisson_distribution(
            mean,
            random_variable_value
        ),
        3
    )
)
