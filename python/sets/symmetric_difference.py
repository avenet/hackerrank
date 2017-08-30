_ = int(input())
first_set = set(map(int, input().split()))

_ = int(input())
second_set = set(map(int, input().split()))

for number in sorted(first_set ^ second_set):
    print(number)
