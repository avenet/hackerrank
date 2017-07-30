def reduce_string(str_array):
    if len(str_array) <= 1:
        return str_array, False
    
    ignore = None
    
    for i in xrange(len(str_array) - 1):
        if str_array[i] == str_array[i+1]:
            ignore = i
            break

    if ignore is None:
        return str_array, False
    
    result = []
    
    for i in xrange(len(str_array)):
        if i != ignore and i != ignore + 1:
            result.append(str_array[i])
    
    return result, True

str_array = list(raw_input())

while True:
    str_array, reduced = reduce_string(str_array)
    if not reduced:
        break
        
if len(str_array) == 0:
    print('Empty String')
else:
    print ''.join(str_array)