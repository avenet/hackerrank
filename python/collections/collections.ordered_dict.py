from collections import OrderedDict

items = int(input())

result = OrderedDict()

for i in range(items):
    item_line = input()
    item_name, item_price_str_value = item_line.strip().rsplit(' ', 1)
    item_price = int(item_price_str_value)
    
    if item_name not in result:
        result[item_name] = item_price
    else:
        result[item_name] += item_price

for item_name, item_price in result.items():
    print('{} {}'.format(item_name, item_price))
