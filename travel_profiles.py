hotel_count = int(raw_input())

hotels = []

for i in xrange(hotel_count):
    hotel_data = raw_input().split()
    hotels.append({
        'id': hotel_data[0],
        'price': int(hotel_data[1]),
        'facilities': set(hotel_data[2::])
    })
    
hotels.sort(cmp=lambda h1, h2: -cmp(len(h1['facilities']), len(h2['facilities'])) or cmp(h1['price'], h2['price']) or cmp(h1['id'], h2['id']))

guest_count = int(raw_input())

for j in xrange(guest_count):
    guest_data = raw_input().split()
    price, facilities = int(guest_data[0]), set(guest_data[1::])
    
    matching_hotels = [str(hotel['id']) for hotel in hotels if price >= hotel['price'] and not len(facilities.difference(hotel['facilities']))]
    print ' '.join(matching_hotels)