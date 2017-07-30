input_string = raw_input()
chunks = int(raw_input())

def divide_in_chunks(input_string, chunks):
    i = 0
    j = chunks
    
    result = []
    
    while i < len(input_string):
        result.append(input_string[i:j])
        i += chunks
        j += chunks
    
    return result

def break_chunk(str_chunk):
    result = ''
    for c in str_chunk:
        if c not in result:
            result += c
    return result

str_chunks = divide_in_chunks(input_string, chunks)
broken_chunks = [break_chunk(x) for x in str_chunks]

for broken_chunk in broken_chunks:
    print broken_chunk