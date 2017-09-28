import re

search_string = input()

string_pattern = input()

pattern_matches = list(
    re.finditer(
        "(?=({}))".format(
            string_pattern
        ),
        search_string
    )
)

if not pattern_matches:
    print((-1, -1))
else:
    for pattern_match in pattern_matches:
        print(
            (
                pattern_match.start(1),
                pattern_match.end(1) - 1
            )
        )
