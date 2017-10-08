import re

CREDIT_CARD_RE = re.compile(
    r'^[4-6][0-9]{3}[-]?[0-9]{4}[-]?[0-9]{4}[-]?[0-9]{4}$'
)

INVALID_NUMBERS_RE = re.compile(
    r'(\d)(?=\1{3})'
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
