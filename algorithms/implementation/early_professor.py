cases = int(input())

for cases in range(cases):
    n, k = map(
        int,
        input().split()
    )
    
    arrivals = map(int, input().split())
    
    early_comers = len([x for x in arrivals if x <= 0])
    
    if early_comers >= k:
        print('NO')
    else:
        print('YES')
