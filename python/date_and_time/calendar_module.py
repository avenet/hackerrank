import calendar

day_names = [
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY',
    'THURSDAY',
    'FRIDAY',
    'SATURDAY',
    'SUNDAY'
]

month, day, year = list(map(int, input().split()))

day_position = calendar.weekday(year, month, day)

print(day_names[day_position])
