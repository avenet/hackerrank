staircase_length = int(raw_input())

for i in xrange(1, staircase_length+1):
    print (' ' * (staircase_length - i))+ ('#' * i))