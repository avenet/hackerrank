def bon_appetit(items_price, refused_item_index, anna_bill):
    total_bill = sum(items_price)
    excluded_item_price = items_price[refused_item_index]
    expected_anna_bill = (total_bill - excluded_item_price) // 2

    if expected_anna_bill == anna_bill:
        return 'Bon Appetit'

    return abs(anna_bill - expected_anna_bill)


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
print(bon_appetit(ar, k, b))
