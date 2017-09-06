s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]

m, n = input().strip().split(' ')
m, n = [int(m), int(n)]

apple_distances = [
    int(apple_temp)
    for apple_temp
    in input().strip().split(' ')
]

orange_distances = [
    int(orange_temp)
    for orange_temp
    in input().strip().split(' ')
]


def count_fruits(initial_point, distances):
    fruits = 0
    
    for distance in distances:
        if s <= initial_point + distance <= t:
            fruits += 1
    
    return fruits


print(count_fruits(a, apple_distances))
print(count_fruits(b, orange_distances))
