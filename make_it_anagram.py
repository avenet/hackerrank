a, b, result = raw_input(), raw_input(), 0

a_chars = set(a)
b_chars = set(b)

for a_char in a_chars:
    if a_char not in b_chars:
        result += a.count(a_char)
    else:
        a_char_count = a.count(a_char)
        b_char_count = b.count(a_char)
        result += abs(a_char_count - b_char_count)
        
for b_char in b_chars:
    if b_char not in a_chars:
        result += b.count(b_char)
        
print result