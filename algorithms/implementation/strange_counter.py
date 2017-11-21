t = int(input().strip())

result = 0

current_time, current_value = 1, 3


def get_next_interval_cycle(time, value):
    next_time = time + value
    next_value = value * 2

    return next_time, next_value


while True:
    new_time, new_value = get_next_interval_cycle(
        current_time,
        current_value
    )

    if new_time > t:
        result = current_value - (t - current_time)
        break
    elif new_time == t:
        result = new_value

    current_time, current_value = new_time, new_value

print(result)
