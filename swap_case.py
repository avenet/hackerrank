input_str = raw_input()

def swap_case(char):
    return char.isupper() and char.lower() or char.upper()

print ''.join(map(swap_case, input_str))