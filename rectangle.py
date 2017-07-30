rectangle_laterals = [(x, 32-x) for x in xrange(1, 31)]

results = []

for x, y in rectangle_laterals:
    division = (x * y) / (x * (y / 31.0)) 
    if division == 31:
        results.append((x,y, x*y, x* (30*y / 31.0)))

res = max(results, key=lambda x : x[3])
print res[2]