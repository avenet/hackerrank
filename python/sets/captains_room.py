from collections import defaultdict

k = int(input())

room_numbers_list = list(
    map(
        int,
        input().split()
    )
)

unique_room_numbers = set(room_numbers_list)

room_number_counter = defaultdict(int)

for room_number in room_numbers_list:
    room_number_counter[room_number] += 1

for unique_room_number, room_count in room_number_counter.items():
    if room_count != k:
        print(unique_room_number)
        break
