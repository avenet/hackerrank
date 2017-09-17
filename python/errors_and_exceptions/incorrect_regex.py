import re

cases = int(input())

for case in range(cases):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
