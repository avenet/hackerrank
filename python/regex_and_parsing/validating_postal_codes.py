import re

POSTAL_CODE_RE = re.compile(r'^[1-9]\d{5}$')

ALTERNATING_DIGITS_RE = re.compile(
    r'(\d)(?=\d\1)'
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
