#!/bin/python3


def stock_purchase_day(stock_prices, price, purchase_buckets):
    begin = None
    end = None

    for bucket_begin, bucket_end, min_bucket_value in purchase_buckets:
        if min_bucket_value <= price:
            begin, end = bucket_begin, bucket_end
            break

    if begin is None:
        return -1

    i = end

    for stock_price in reversed(stock_prices[begin: end]):
        if stock_price <= price:
            return i
        i -= 1

    return -1


def build_buckets(items, bucket_size):
    bucket_result = []
    ini = 0
    item_count = len(items)

    while ini < item_count:
        end = ini + bucket_size

        if end >= item_count:
            end = item_count

        current_min = min(items[ini: end])
        bucket_result.append((ini, end, current_min))
        ini += bucket_size

    bucket_result.reverse()

    return bucket_result


n = int(input().strip())
numbers = list(map(int, input().strip().split(' ')))
buckets = build_buckets(numbers, 1000)

q = int(input().strip())

for a0 in range(q):
    xi = int(input().strip())
    result = stock_purchase_day(numbers, xi, buckets)
    print(result)
