testcases = int(raw_input())

def is_palindrome(input_str, ignore):
    i = 0
    j = len(input_str) - 1
    
    while i < j:
        if i == ignore:
            i += 1
        
        if j == ignore:
            j -= 1
        
        if input_str[i] != input_str[j]:
            return False
        
        i += 1
        j -= 1
        
        if i == ignore:
            i += 1
        
        if j == ignore:
            j -= 1
    
    return True

for testcase in xrange(testcases):
    input_str = raw_input()
    
    i = 0
    j = len(input_str) - 1
    
    result = -1
    
    while i < j:
        if input_str[i] != input_str[j]:
            if is_palindrome(input_str, i):
                result = i
            elif is_palindrome(input_str, j):
                result = j
            break
        i+=1
        j-=1
    
    print result
     