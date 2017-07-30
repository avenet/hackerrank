
for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print sum(list(map(lambda x: x[1] * 10**(2*(i-1) - x[0]), enumerate(range(1, i+1)))) + list(map(lambda x: x[1] * 10**x[0], enumerate(range(1, i+1))))[::-1][1:]) 