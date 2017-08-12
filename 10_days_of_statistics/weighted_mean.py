n = int(input())
elements = map(int, input().split())
weights = map(int, input().split())

result = 0
sum_of_weights = 0

for e, w in zip(elements, weights):
    result += e * w
    sum_of_weights += w

result = result / float(sum_of_weights)

print(round(result, 1))