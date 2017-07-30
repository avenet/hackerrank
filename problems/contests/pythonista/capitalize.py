l = list(raw_input())

cap = True

for i, c in enumerate(l):
    if cap and c != ' ':
        cap = False
        l[i] = c.upper()
    elif c == ' ':
        cap = True

print ''.join(l)