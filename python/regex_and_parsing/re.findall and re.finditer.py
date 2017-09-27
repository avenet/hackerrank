import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

surrounded_vowels_re = r'[%s](?P<substr>[%s]{2,})(?=[%s])' % (
    consonants,
    vowels,
    consonants
)

matches = re.findall(
    surrounded_vowels_re,
    input(),
    flags=re.I
)

if matches:
    for match in matches:
        print(match)
else:
    print(-1)
