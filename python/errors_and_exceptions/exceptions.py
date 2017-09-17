cases = int(input())

for case in range(cases):
    try:
        numerator, denominator = map(int, input().split())
        print(numerator // denominator)
    except Exception as exc:
        print("Error Code: {}".format(exc))
