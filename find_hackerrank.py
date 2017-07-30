import re

cases = int(raw_input())

startswith_hackerrank_re = re.compile('^hackerrank')
endswith_hackerrank_re = re.compile('.*?hackerrank$')

for case in xrange(cases):
    case_str = raw_input()
    startswith_hackerrank = startswith_hackerrank_re.match(case_str)
    endswith_hackerrank = endswith_hackerrank_re.match(case_str)
    
    if startswith_hackerrank and endswith_hackerrank:
        print('0')
    elif startswith_hackerrank:
        print('1')
    elif endswith_hackerrank:
        print('2')
    else:
        print('-1')