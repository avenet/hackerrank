import re

NON_BEAUTIFUL_PART = re.compile('010')


def min_steps(number):
    return len(
        NON_BEAUTIFUL_PART.findall(
            number
        )
    )


n = int(input().strip())

binary_str = input().strip()
result = min_steps(binary_str)

print(result)
