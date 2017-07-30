testcases = int(raw_input())

for testcase in xrange(testcases):
    input_str = raw_input()
    input_length = len(input_str) % 2
    if input_length == 1:
        print -1
        continue
    
    input_half = len(input_str) / 2
    
    first_half = input_str[0: input_half]
    second_half = input_str[input_half: ]
    
    unique_characters = set(input_str)
    result = 0
    
    for unique_character in unique_characters:
        first_count = first_half.count(unique_character)
        second_count = second_half.count(unique_character)
        
        result += abs(first_count - second_count)
    
    print result / 2