import re

UID_RE = re.compile(r'^[a-zA-Z0-9]{10}$')
TWO_UPPERCASE_LETTERS_RE = re.compile(r'^[a-z0-9]*[A-Z][a-z0-9]*[A-Z][a-zA-Z0-9]*$')
AT_LEAST_THREE_DIGITS_RE = re.compile(r'^[a-zA-Z]*[0-9][a-zA-Z]*[0-9][a-zA-Z]*[0-9][a-zA-Z0-9]*$')


def check_uid(str_value):
    return (
        UID_RE.match(str_value) and
        len(set(str_value)) == len(str_value) and
        TWO_UPPERCASE_LETTERS_RE.search(str_value) and
        AT_LEAST_THREE_DIGITS_RE.match(str_value)
    )


cases = int(input())

for case_number in range(cases):
    is_valid_uuid = check_uid(input())
    
    if is_valid_uuid:
        print('Valid')
    else:
        print('Invalid')
