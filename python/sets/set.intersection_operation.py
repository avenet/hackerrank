_ = int(input())
first_set = set(map(int, input().split()))

_ = int(input())
second_set = set(map(int, input().split()))

print(len(first_set & second_set))
