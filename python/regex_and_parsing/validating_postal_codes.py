import re

POSTAL_CODE_RE = re.compile(r'^[1-9]\d{5}$')

ALTERNATING_DIGITS_RE = re.compile(
    r'0(?=\d0)|'
    r'1(?=\d1)|'
    r'2(?=\d2)|'
    r'3(?=\d3)|'
    r'4(?=\d4)|'
    r'5(?=\d5)|'
    r'6(?=\d6)|'
    r'7(?=\d7)|'
    r'8(?=\d8)|'
    r'9(?=\d9)'
)

input_str = input()

print(
    POSTAL_CODE_RE.match(input_str) is not None
    and len(
        ALTERNATING_DIGITS_RE.findall(
            input_str
        )
    ) <= 1
)
