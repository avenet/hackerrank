from email.utils import formataddr, parseaddr

import re

emails_to_validate = int(input())

EMAIL_RE = re.compile(
    r'^[a-zA-Z][a-zA-Z0-9\._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
)


def validate_email(email_guess):
    return bool(EMAIL_RE.match(email_guess))


for i in range(emails_to_validate):
    real_name, email_address = parseaddr(input())

    if not real_name and not email_address:
        continue

    if not validate_email(email_address):
        continue

    print(formataddr((real_name, email_address)))
