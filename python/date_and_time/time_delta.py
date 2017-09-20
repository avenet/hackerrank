#!/bin/python3
from datetime import datetime


def to_date(date_str):
    return datetime.strptime(
        date_str,
        '%a %d %b %Y %H:%M:%S %z'
    )


def time_delta(t1, t2):
    first_date = to_date(t1)
    second_date = to_date(t2)

    delta_time = first_date - second_date

    return abs(
        int(
            delta_time.total_seconds()
        )
    )


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
