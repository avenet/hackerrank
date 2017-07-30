import re

testcases = int(raw_input())
result = 0

for x in xrange(testcases):
    if re.search('hackerrank', raw_input(), re.IGNORECASE):
        result += 1

print result