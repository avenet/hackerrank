import re

n = int(input())


def replace_operator(match):
    operator = match.group(0)

    if operator == '&&':
        return 'and'
    elif operator == '||':
        return 'or'

    return operator


input_data = []

for i in range(n):
    input_data.append(input())

input_str = '\n'.join(input_data)

print(
    re.sub(
        r"(?<= )(&&|\|\|)(?= )",
        replace_operator,
        input_str
    )
)
