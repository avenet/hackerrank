cases = int(raw_input())

def get_minimum_operations(str_input):
    result = 0
    i = 0
    j = len(str_input) - 1
    
    while i < j:
        left_char = str_input[i]
        right_char = str_input[j]
        result += abs(ord(left_char) - ord(right_char))
        i+=1
        j-=1
    
    return result

for case in xrange(cases):
    str_input = raw_input()
    minimum_operations = get_minimum_operations(str_input)
    print minimum_operations