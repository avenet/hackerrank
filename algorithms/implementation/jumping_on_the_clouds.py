def can_jump(cloud_list, current_position, jump_length):
    next_position = current_position + jump_length

    return (
        next_position < len(cloud_list) and
        cloud_list[next_position] == 0
    )


def get_min_steps(cloud_list):
    emma_position = 0
    min_steps = 0
    cloud_length = len(cloud_list)

    while emma_position < cloud_length - 1:
        if can_jump(cloud_list, emma_position, 2):
            emma_position += 2
            min_steps +=1
        elif can_jump(cloud_list, emma_position, 1):
            emma_position += 1
            min_steps +=1
        else:
            return -1

    return min_steps


n = int(input().strip())


clouds = [
    int(c_temp)
    for c_temp
    in input().strip().split(' ')
]

print(get_min_steps(clouds))
