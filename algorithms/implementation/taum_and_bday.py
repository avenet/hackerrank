t = int(
    input().strip()
)

for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b),int(w)]

    x, y, z = input().strip().split(' ')
    x, y, z = int(x), int(y), int(z)

    min_black_price = min(b*x, b*(y+z))
    min_white_price = min(w*y, w*(x+z))

    print(min_black_price + min_white_price)
