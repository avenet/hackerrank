import re

CREDIT_CARD_RE = re.compile(
    r'^[4-6][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}$'
)

INVALID_NUMBERS_RE = re.compile(
    r'0000|1111|2222|3333|4444|5555|6666|7777|8888|9999'
)

credit_card_numbers = int(input())

for case in range(credit_card_numbers):
    credit_card_candidate = input()
    
    credit_card_matches = CREDIT_CARD_RE.match(
        credit_card_candidate
    )
    
    if credit_card_matches:
        numbers = credit_card_candidate.replace('-', '')
        if INVALID_NUMBERS_RE.findall(numbers):
            print('Invalid')
        else:
            print('Valid')
    
    else:
        print('Invalid')
