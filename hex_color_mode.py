import re

css_color_re = re.compile("(#(?:[0-9a-fA-F])+)")
lines = int(raw_input())
find_regex = False

def print_found_colors(line):
    for match in css_color_re.findall(line):
        if len(match) == 4 or len(match) == 7:
            print match

for i in xrange(lines):
    line = raw_input().strip()
    if '{' in line:
        find_regex = True
    elif '}' in line:
        find_regex = False
    elif find_regex:
        print_found_colors(line)