from bisect import bisect_left


def get_distance(
    stations,
    station,
    position,
    total_stations
):
    left_station_position = position
    right_station_position = position - 1

    stations_length = len(stations)

    left_distance = total_stations
    right_distance = total_stations

    if 0 <= left_station_position < stations_length:
        left_distance = abs(
            station - stations[left_station_position]
        )

    if 0 <= right_station_position < stations_length:
        right_distance = abs(
            station - stations[right_station_position]
        )

    return min(left_distance, right_distance)


n, m = map(
    int,
    input().strip().split(' ')
)

stations = [
    int(c_temp)
    for c_temp
    in input().strip().split(' ')
]

stations.sort()

max_distance = 0

for i in range(n):
    position = bisect_left(stations, i)
    current_distance = get_distance(stations, i, position, n)

    if current_distance > max_distance:
        max_distance = current_distance

print(max_distance)
