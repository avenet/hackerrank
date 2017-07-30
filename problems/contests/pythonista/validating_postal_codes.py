def contains_only_digits(str_input):
    result = True
    for char in str_input:
        result = result and char.isdigit()
    return str_input and result

def is_in_range(str_input):
    return 100000 <= int(str_input) <= 999999

def alternative_digits(str_input):
    even_items = str_input[::2]
    odd_items = str_input[1::2]
    
    result = 0
    
    last_char = None
    
    for item in even_items:
        result += (last_char == item)
        last_char = item
    
    last_char = None
    
    for item in odd_items:
        result += (last_char == item)
        last_char = item
        
    return result

str_input = raw_input()
print contains_only_digits(str_input) and is_in_range(str_input) and alternative_digits(str_input) <= 1