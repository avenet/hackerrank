from collections import defaultdict


def get_delete_count(array):
    counter_dict = defaultdict(int)
    
    for item in array:
        counter_dict[item] += 1
    
    max_repetitions = max(
        counter_dict.values()
    )
    
    return len(array) - max_repetitions


_ = input()

array_items = list(
    map(
        int,
        input().split()
    )
)

print(get_delete_count(array_items))
