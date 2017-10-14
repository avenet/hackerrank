#!/bin/python3


def stock_purchase_day(stock_prices, xi, buckets):
    begin = None
    end = None
    
    for bucket_begin, bucket_end, min_bucket_value in buckets:
        if min_bucket_value <= xi:
            begin, end = bucket_begin, bucket_end
            break
    
    if begin is None:
        return -1
    
    i = end
    
    for stock_price in reversed(stock_prices[begin: end]):
        if stock_price <= xi:
            return i
        i -= 1
    
    return -1


def build_buckets(numbers, bucket_size):
    buckets = []
    ini = 0
    n = len(numbers)
    
    while ini < n:
        end = ini + bucket_size
        
        if end >= n:
            end = n
        
        current_min = min(numbers[ini: end])
        buckets.append((ini, end, current_min))
        ini += bucket_size
    
    buckets.reverse()
    
    return buckets


n = int(input().strip())
numbers = list(map(int, input().strip().split(' ')))
buckets = build_buckets(numbers, 1000)

q = int(input().strip())

for a0 in range(q):
    xi = int(input().strip())
    result = stock_purchase_day(numbers, xi, buckets)
    print(result)
