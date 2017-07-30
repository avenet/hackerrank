testcases = int(raw_input())

def is_equal(d1, d2):
    if len(d1) != len(d2):
        return False
        
    for k, v in d1.items():
        if k != 'last':
            if d1[k] != d2.get(k):
                return False

    return True
    
def next_level(dict_items):
    next_level_result = []
    
    for i in xrange(len(dict_items) - 1):
        dict_item = dict_items[i]
        next_last_char = dict_items[i + 1]['last']
        dict_item['last'] = next_last_char
        dict_item[next_last_char] = dict_item.get(next_last_char, 0) + 1
        next_level_result.append(dict_item)
        
    return next_level_result

for testcase in xrange(testcases):
    input_str = raw_input()
    
    dict_items = []
    result = 0
    
    for c in input_str:
        dict_item = {'last': c}
        dict_item[c] = 1
        dict_items.append(dict_item)
        
    while len(dict_items) > 1:
        for i in xrange(len(dict_items)):
            for j in xrange(i+1, len(dict_items)):
                if is_equal(dict_items[i], dict_items[j]):
                    result += 1
        
        dict_items = next_level(dict_items)
        
    print result