def build_letters(letters):
    result = list(letters)
    
    if len(result) > 1:
        result = result[1:][::-1] + result
    
    return result


def print_rangoli(size):
    line_size = 2 * (size - 1)
    letters = [
        chr(96 + size)
    ]
    
    printed_items = []
    
    for i in range(1, size + 1):
        surroundings = '-' * line_size
        letter_items = build_letters(letters)
        
        to_print = '{0}{1}{0}'.format(
            surroundings,
            '-'.join(letter_items)
        )
        
        print(to_print)
        
        if i != size:
            printed_items.append(to_print)
        
        first_letter = ord(letters[0])
        previous_letter = chr(first_letter - 1)
        letters.insert(0, previous_letter)
        line_size -= 2
    
    for reversed_printed_item in reversed(printed_items):
        print(reversed_printed_item)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
