n = int(input())

for i in range(n):
    money, item_price, exchange_wrapper = [int(x) for x in input().split(' ')]
    bought = money // item_price
    answer = bought
    wrappers = bought
    
    while wrappers >= exchange_wrapper:
        extra_items = wrappers // exchange_wrapper
        answer += extra_items
        wrappers = (wrappers % exchange_wrapper) + extra_items
    
    print(int(answer))
