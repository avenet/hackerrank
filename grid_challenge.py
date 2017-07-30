testcases = int(raw_input())

for testcase in xrange(testcases):
    grid_size = int(raw_input())
    grid_vertical_words = ['' for x in xrange(grid_size)]
    
    answer = 'YES'
    
    for _ in xrange(grid_size):
        grid_word = raw_input()
        for i, c in enumerate(sorted(grid_word)):
            grid_vertical_words[i] += c
    
    for vertical_word in grid_vertical_words:
        for j in xrange(len(grid_vertical_words) - 1):
            if vertical_word[j] > vertical_word[j+1]:
                answer = 'NO'
                break
    
    print answer