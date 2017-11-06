#!/bin/python3


def is_thundercloud(clouds, cloud_position):
    return clouds[cloud_position] == 1


def get_energy(clouds, step, initial_energy=100):
    current_position = 0
    current_energy = initial_energy
    cloud_count = len(clouds)
    
    while True:
        current_position = (current_position + step) % cloud_count
        
        current_energy -= 1
        
        if is_thundercloud(clouds, current_position):
            current_energy -= 2
        
        if current_position == 0:
            break
    
    return current_energy


_, cloud_step = map(
    int,
    input().strip().split(' ')
)

param_clouds = [
    int(c_temp)
    for c_temp
    in input().strip().split(' ')
]

print(
    get_energy(
        param_clouds,
        cloud_step
    )
)
