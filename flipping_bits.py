cases = int(raw_input())

def flip(c):
    if c == '0':
        return '1'
    return '0'

for case in xrange(cases):
    number = int(raw_input())
    binary_number = bin(number).replace('0b', '')
    if len(binary_number) < 32:
        binary_number = '0' * (32 - len(binary_number)) + binary_number
    binary_number = ''.join([flip(c) for c in binary_number])
    print int(binary_number, 2)