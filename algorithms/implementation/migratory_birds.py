def get_most_common_bird_type(bird_types):
    bird_type_occurrences_map = {
        i: 0
        for i in range(1, 6)
    }
    
    for bird_type in bird_types:
        bird_type_occurrences_map[bird_type] += 1
    
    most_common_bird_type = 0
    max_bird_type_occurrences = 0
    
    for i in range(1, 6):
        if bird_type_occurrences_map[i] > max_bird_type_occurrences:
            most_common_bird_type = i
            max_bird_type_occurrences = bird_type_occurrences_map[i]
    
    return most_common_bird_type


n = int(input().strip())

bird_types_list = list(
    map(
        int,
        input().strip().split(' ')
    )
)

print(
    get_most_common_bird_type(
        bird_types_list
    )
)
