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


def get_leaderboard_position(current_leaderboard, target_score):
    min_value = current_leaderboard[-1]

    if target_score == min_value:
        return len(current_leaderboard)
    elif target_score < min_value:
        return 1 + len(leaderboard)

    position = 1

    for leader_score in current_leaderboard:
        if target_score >= leader_score:
            return position
        position += 1

    return position


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
