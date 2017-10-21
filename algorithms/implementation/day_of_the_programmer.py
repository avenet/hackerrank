def julian_is_leap(year):
    return year % 4 == 0


def gregorian_is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def solve(year):
    month = '09'
    day = '13'

    if year <= 1917:
        is_leap_year = julian_is_leap(year)
    elif year == 1918:
        day = '26'
        is_leap_year = False
    else:
        is_leap_year = gregorian_is_leap(year)

    if is_leap_year:
        day = '12'

    return '{}.{}.{}'.format(
        day,
        month,
        year,
    )


input_year = int(input().strip())
print(solve(input_year))
