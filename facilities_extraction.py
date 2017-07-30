facility_count = int(raw_input())

facilities = []

for i in xrange(facility_count):
    facilities.append(raw_input())

facilities.sort()
    
description = raw_input().lower()

print '\n'.join(sorted([f for f in facilities if f.lower() in description]))