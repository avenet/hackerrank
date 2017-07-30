T = int(raw_input())

for i in range (0,T):
    money, item_price, exchange_wrapper = [int(x) for x in raw_input().split(' ')]
    bought = money / item_price
    answer = bought
    wrappers = bought
    
    while wrappers >= exchange_wrapper:
        extra_items = wrappers / exchange_wrapper
        answer += extra_items
        wrappers = (wrappers % exchange_wrapper) + extra_items
    
    print answer
