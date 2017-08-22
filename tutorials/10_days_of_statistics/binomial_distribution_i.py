from functools import reduce
from operator import mul

a, b = map(float, input().split())

n, x = 6, 3

p = a / (a + b)
q = 1 - p


def fact(number):
    if number == 0:
        return 1
    
    return reduce(
        mul,
        range(1, number + 1)
    )


def binomial(total, desired_samples, probability):
    inverse_probability = 1 - probability

    permutations = fact(total) / (
        fact(desired_samples) * fact(total - desired_samples)
    )
    
    probability_mult = (
        probability ** desired_samples
    ) * (
        inverse_probability ** (total - desired_samples)
    )
    
    return permutations * probability_mult


result = sum(
    [
        binomial(n, k, p)
        for k
        in range(x, n + 1)
    ]
)

print(round(result, 3))
