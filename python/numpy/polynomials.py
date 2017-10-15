import numpy

poly_coefficients = list(
    map(
        float,
        input().split()
    )
)

x_value = int(input())

print(
    numpy.polyval(
        poly_coefficients,
        x_value
    )
)
