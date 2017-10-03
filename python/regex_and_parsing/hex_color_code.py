import re

line_count = int(input())

css_lines = []

for line in range(line_count):
    css_lines.append(input())

css_text = '\n'.join(css_lines)

match_occurrences = re.findall(
    r'#[0-9A-Fa-f]{3,6}(?!\s+{)',
    css_text
)

for match_occurrence in match_occurrences:
    print(match_occurrence)
