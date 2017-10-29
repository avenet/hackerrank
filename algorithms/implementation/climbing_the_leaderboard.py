import sys


def get_leaderboard(player_scores):
    result = []
    
    leaderboard_scores = sorted(
        player_scores,
        reverse=True
    )
    
    previous_score = sys.maxsize
    
    for leaderboard_score in leaderboard_scores:
        if previous_score != leaderboard_score:
            result.append(leaderboard_score)
        
        previous_score = leaderboard_score
    
    return result


def binary_search(leaderboard_values, score):
    i = 0
    j = len(leaderboard_values) - 1
    
    if score <= leaderboard_values[-1]:
        return j
    elif score == leaderboard_values[0]:
        return 0
    elif score > leaderboard_values[0]:
        return -1
    
    while i < j:
        mid = (j + i) // 2
        middle_element = leaderboard_values[mid]
        
        if mid == i:
            return i
        
        if score > middle_element:
            j = mid
        elif score < middle_element:
            i = mid
        else:
            return mid
    
    if leaderboard_values[j] > score:
        return j
    
    return i


def get_leaderboard_position(current_leaderboard, target_score):
    position = binary_search(
        current_leaderboard,
        target_score
    )
    
    result = 1 + position
    
    if current_leaderboard[position] == target_score:
        return result
    
    return 1 + result


n = int(input().strip())

scores = [
    int(scores_temp)
    for scores_temp
    in input().strip().split(' ')
]

m = int(input().strip())

alice_scores = [
    int(alice_temp)
    for alice_temp
    in input().strip().split(' ')
]

leaderboard = get_leaderboard(scores)

for alice_score in alice_scores:
    print(
        get_leaderboard_position(
            leaderboard,
            alice_score
        )
    )
