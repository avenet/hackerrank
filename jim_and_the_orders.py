order_count = int(raw_input())

orders = []

for order in xrange(1, order_count + 1):
    init, time = map(int, raw_input().split())
    orders.append((order, init + time))
    
orders.sort(key=lambda x: x[1])

print ' '.join([str(order[0]) for order in orders])