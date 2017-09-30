# Borrowed from http://bit.ly/2kcMA7i

import re

ROMAN_NUMERAL = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

print(bool(ROMAN_NUMERAL.match(input())))
