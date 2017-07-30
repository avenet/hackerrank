N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0
result = 0
flower_count = 0
x = 0
k = 0

for number in numbers.split():
    C.append(int(number))

C.sort(reverse=True)

for number in C:
    k += 1
    if k == K + 1:
        x += 1
        k = 1
    flower_price = (x+1)*int(number)
    result += flower_price

print result