hour = int(raw_input())
minutes = int(raw_input())



number_map = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty one',
    22: 'twenty two',
    23: 'twenty three',
    24: 'twenty four',
    25: 'twenty five',
    26: 'twenty six',
    27: 'twenty seven',
    28: 'twenty eight',
    29: 'twenty nine',
    30: 'thirty',
}

if not minutes:
    print "%s o' clock" % number_map[hour]
elif minutes == 15:
    print "quarter past %s" % number_map[hour]
elif 1 <= minutes <= 29:
    pluralize_minutes = minutes > 1 and 'minutes' or 'minute'
    print "%s %s past %s" % (number_map[minutes], pluralize_minutes, number_map[hour])
elif minutes == 30:
    minutes = minutes > 1 and 'minutes' or 'minute'
    print "half past %s" % number_map[hour]
elif minutes == 45:
    print "quarter to %s" % number_map[(hour + 1)]
else:
    minutes_left = 60 - minutes
    pluralize_minutes = minutes_left > 1 and 'minutes' or 'minute'
    print "%s %s to %s" % (number_map[minutes_left], pluralize_minutes, number_map[(hour + 1)])