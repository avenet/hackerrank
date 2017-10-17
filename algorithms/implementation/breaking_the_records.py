def get_record(season_scores):
    highest_score = season_scores[0]
    lowest_score = season_scores[0]

    best_score_increased_times = 0
    worst_score_increased_times = 0

    for score in season_scores[1:]:
        if score < lowest_score:
            lowest_score = score
            worst_score_increased_times += 1
        elif score > highest_score:
            highest_score = score
            best_score_increased_times += 1

    return (
        best_score_increased_times,
        worst_score_increased_times
    )


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = get_record(s)
print(" ".join(map(str, result)))
