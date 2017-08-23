from functools import reduce
from operator import mul

p, n = map(float, input().split())

p /= 100.0
n = int(n)

q, x = 1 - p, 2


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
        in range(0, x + 1)
    ]
)

p_no_more_than_two_rejects = round(result, 3)
p_at_least_two_rejects = round(
    1.0 - p_no_more_than_two_rejects + binomial(n, x, p),
    3
)

print(p_no_more_than_two_rejects)
print(p_at_least_two_rejects)
