import re

input_str = input()

for str_part in re.split('[,\.]', input_str.strip()):
    if str_part:
        print(str_part)
