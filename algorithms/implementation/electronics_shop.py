def get_spent_money(keyboard_prices, drive_prices, money_to_spend):
    best_result = -1

    for keyboard_price in keyboard_prices:
        for drive_price in drive_prices:
            current_price = keyboard_price + drive_price
            if best_result < current_price <= money_to_spend:
                best_result = current_price

    return best_result


gift_budget, _, _ = map(int, input().strip().split(' '))
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

spent_money = get_spent_money(keyboards, drives, gift_budget)

print(spent_money)
