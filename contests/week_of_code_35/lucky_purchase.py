def is_valid_price(price):
    fours = 0
    sevens = 0
    
    for c in str(price):
        if c == '4':
            fours += 1
        elif c == '7':
            sevens += 1
        else:
            return False
    
    return fours == sevens


if __name__ == "__main__":
    n = int(input().strip())
    best_laptop_name = None
    best_price = None
    
    for a0 in range(n):
        name, value = input().strip().split(' ')
        name, value = [str(name), int(value)]
        
        is_valid = is_valid_price(value)
        
        if is_valid:
            if best_price is None or value < best_price:
                best_price = value
                best_laptop_name = name
    
    print(
        -1
        if best_laptop_name is None
        else best_laptop_name
    )
