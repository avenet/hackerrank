def get_kth_item_key(k):
    def key_function(items_list):
        return items_list[k]
    return key_function


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []

    for arr_i in range(n):
        arr_t = [
           int(arr_temp)
           for arr_temp
           in input().strip().split(' ')
        ]

        arr.append(arr_t)

    k = int(input().strip())

    for items in sorted(
        arr,
        key=get_kth_item_key(k)
    ):
        print(' '.join(map(str, items)))
