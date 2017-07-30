cases = int(raw_input())

for case in xrange(cases):
    cc_number = raw_input()
    valid = True
    
    if len(cc_number) < 16 or cc_number[0] not in ['4', '5', '6']:
        valid = False
    
    digits = list(filter(str.isdigit, cc_number))
    
    if len(digits) != 16:
        valid = False
    
    invalid_chars = list(filter(lambda x: not x.isdigit and x != '-', cc_number))
    
    if len(invalid_chars) > 0:
        valid = False
    
    if '-' in cc_number:
        dig_groups = cc_number.split('-')
        
        if len(dig_groups) == 4:
            for dig_group in dig_groups:
                if len(dig_group) != 4:
                    valid = False
                    break
        else:
            valid = False
            
    last_digit = None
    ocurrences = 0
    
    for digit in digits:
        if digit != last_digit:
            last_digit = digit
            ocurrences = 1
        else:
            ocurrences += 1
            if ocurrences == 4:
                valid = False
                break
        
    if not valid:
        print 'Invalid'
    else:
        print 'Valid'