from datetime import date

actual_date_parts = list(
    map(
        int,
        input().split()
    )
)

expected_date_parts = list(
    map(
        int,
        input().split()
    )
)

actual_date = date(
    actual_date_parts[2],
    actual_date_parts[1],
    actual_date_parts[0]
)

expected_date = date(
    expected_date_parts[2],
    expected_date_parts[1],
    expected_date_parts[0]
)

elapsed = expected_date - actual_date
elapsed_days = elapsed.days

if elapsed_days >= 0:
    print(0)
elif actual_date.month == expected_date.month and actual_date.year == expected_date.year:
    print(15 * abs(elapsed_days))
elif actual_date.year == expected_date.year:
    print(500 * abs(actual_date.month - expected_date.month))
else:
    print(10000)
