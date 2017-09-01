def get_subsequence(str_value):
    used_characters = {}
    str_chars = []
    
    for char in str_value:
        if char not in used_characters:
            str_chars.append(char)
            used_characters[char] = True
    
    return ''.join(str_chars)


def merge_the_tools(string, k):
    ini = 0
    while ini < len(string):
        current_sequence = string[ini:ini + k]
        print(get_subsequence(current_sequence))
        ini += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)