#!/bin/python3


def maximize_profit(
    currency_to_dollar_rate,
    quantities_for_every_bitcoin,
    ron_bitcoin_quantity,
    bitcoin_conversion_rate
):
    best_profit = bitcoin_conversion_rate * ron_bitcoin_quantity

    for value_in_dollars, currency_quantity in zip(
            currency_to_dollar_rate,
            quantities_for_every_bitcoin
    ):
        current_profit = value_in_dollars * currency_quantity * ron_bitcoin_quantity

        if current_profit > best_profit:
            best_profit = current_profit

    return best_profit


if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]

    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    result = maximize_profit(a, b, m, k)

    print(result)
