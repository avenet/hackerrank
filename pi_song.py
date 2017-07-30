cases = int(raw_input())

pi_value = "31415926535897932384626433833"

for case in xrange(cases):
    str_val = raw_input()
    setence_number = ''.join([str(len(part)) for part in str_val.split()])
    
    if pi_value.startswith(setence_number):
        print "It's a pi song."
    else:
        print "It's not a pi song."