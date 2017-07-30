from itertools import product

k, m = map(int, raw_input().split())

iterables = []
max_product = 0

for x in xrange(k):
    iterables.append(map(lambda x: int(x) ** 2, raw_input().split()[1:]))
    
for product_tuple in product(*iterables):
    max_product = max(sum(product_tuple) % m, max_product)
    
print max_product