def collatzSequenceSum(T, A, B):
    cache = {}

    def collatzSequenceLen(k):
        if k in cache:
            return cache[k]

        if k == 0:
            sequence_result = 0
        if k == 1:
            sequence_result = 1
        elif k % 2 == 0:
            sequence_result = 1 + collatzSequenceLen(k / 2)
        else:
            sequence_result = 1 + collatzSequenceLen(3 * k + 1)

        cache[k] = sequence_result

        return sequence_result
    
    n = 0
    result = 0

    for _ in range(T):
        n = (A * n + B) % 5003
        best_len = 0
        best_num = 0

        for k in range(1, n + 1):
            cur_len = collatzSequenceLen(k)

            if cur_len >= best_len:
                best_len = cur_len
                best_num = k

        result += best_num

    return result


if __name__ == "__main__":
    T, A, B = input().strip().split(' ')
    T, A, B = [int(T), int(A), int(B)]
    result = collatzSequenceSum(T, A, B)
    print(result)
