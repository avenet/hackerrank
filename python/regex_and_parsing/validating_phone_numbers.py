import re

VALID_PHONE_NUMBER = re.compile(r'^[7-9][0-9]{9}$')

test_cases = int(input())

for test_case in range(test_cases):
    is_match = VALID_PHONE_NUMBER.match(input())
    print(is_match and 'YES' or 'NO')
