n = int(input())

p_values = map(
    int,
    input().split()
)

p_reverse_dict = {
    value: i + 1
    for i, value
    in enumerate(p_values)
}

for i in range(1, n + 1):
    reverse_p = p_reverse_dict[i]
    print(p_reverse_dict[reverse_p])
