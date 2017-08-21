#!/bin/python3
def birthday_cake_candles(candle_heights):
    tallest_candle_height = max(candle_heights)

    return candle_heights.count(
        tallest_candle_height
    )

n = int(input().strip())

candles = list(
    map(
        int,
        input().strip().split(' ')
    )
)

result = birthday_cake_candles(candles)

print(result)
