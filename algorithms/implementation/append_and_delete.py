def get_prefix_length(source, target):
    min_length = min(len(source), len(target))
    result = 0

    for i in range(min_length):
        if source[i] != target[i]:
            break
        result += 1

    return result


def can_form_target_string(source, target, steps):
    prefix_length = get_prefix_length(source, target)
    combined_length = len(source) + len(target)

    if k % 2 == combined_length % 2:
        min_operations = combined_length - 2 * prefix_length
    else:
        min_operations = combined_length + 1

    return steps >= min_operations


s = input().strip()
t = input().strip()
k = int(input().strip())


if can_form_target_string(s, t, k):
    print('Yes')
else:
    print('No')
