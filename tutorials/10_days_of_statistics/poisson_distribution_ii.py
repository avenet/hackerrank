

def get_maintenance_cost(
    mean,
    remainder,
    factor=40,
    decimal_places=3
):
    expected_value_variable_squared = mean + (mean ** 2)

    return round(
        remainder + (expected_value_variable_squared * factor),
        decimal_places
    )


a_mean, b_mean = map(float, input().split())

print(
    get_maintenance_cost(a_mean, 160, 40)
)

print(
    get_maintenance_cost(b_mean, 128, 40)
)
