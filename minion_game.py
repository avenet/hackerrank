word = raw_input()

stuart_points = 0
kevin_points = 0

word_length = len(word)

i = 0

for c in word:
    is_vowel = c in 'AEIOU'
    awarded_points = word_length - i
    if is_vowel:
        kevin_points += awarded_points
    else:
        stuart_points += awarded_points
    i += 1

if stuart_points > kevin_points:
    print 'Stuart %s' % stuart_points
elif kevin_points > stuart_points:
    print 'Kevin %s' % kevin_points
else:
    print 'Draw'