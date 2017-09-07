def kangaroo(x1, v1, x2, v2):
    value = v1 - v2
    diff = x2 - x1
    
    if not value:
        return 'NO'
    
    is_divisible = abs(diff) % abs(value) == 0
    
    return (
               is_divisible and diff / value > 0
           ) and 'YES' or 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
