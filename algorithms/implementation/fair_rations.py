def get_distribution_steps(distribution):
    i = 0
    distributed_loaves = 0
    
    while i < len(distribution):
        if distribution[i] % 2 == 0:
            i += 1
            continue
        
        next_item_index = i + 1
        
        if next_item_index == len(distribution):
            return -1
        
        distribution[next_item_index] += 1
        
        distributed_loaves += 2
        i += 1
    
    return distributed_loaves


N = int(input().strip())

current_distribution = [
    int(B_temp)
    for B_temp
    in input().strip().split(' ')
]

steps = get_distribution_steps(current_distribution)
print(steps if steps != -1 else 'NO')
