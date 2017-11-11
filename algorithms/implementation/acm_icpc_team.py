def get_common_topics(first_topics, second_topics):
    result = 0
    
    for i in range(len(first_topics)):
        if first_topics[i] or second_topics[i]:
            result += 1
    
    return result


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]

topic = []

for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(list(map(int, topic_t)))

max_common_topics = 0
teams_with_max_topics = 0

for i in range(n):
    for j in range(i + 1, n):
        current_common_topics = get_common_topics(
            topic[i],
            topic[j]
        )
        
        if current_common_topics > max_common_topics:
            max_common_topics = current_common_topics
            teams_with_max_topics = 1
        elif current_common_topics == max_common_topics:
            teams_with_max_topics += 1


print(max_common_topics)
print(teams_with_max_topics)
