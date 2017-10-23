from collections import defaultdict


def sock_merchant(sock_colors):
    sock_counter = defaultdict(int)
    result = 0

    for sock_color in sock_colors:
        sock_counter[sock_color] += 1

    for sock_type_count in sock_counter.values():
        result += sock_type_count // 2

    return result


n = int(input().strip())
sock_array = list(map(int, input().strip().split(' ')))
print(sock_merchant(sock_array))
