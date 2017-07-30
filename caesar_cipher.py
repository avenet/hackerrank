length = int(raw_input())
encrypt_str = raw_input()
k = int(raw_input())

def encrypt(str_input, k):
    result = ""
    for char in str_input:
        char_number = ord(char)
        if 65 <= char_number <= 90 or 97 <= char_number <= 122:
            is_upper = char.upper() == char
            char = char.lower()
            index = (ord(char) - 97 + k) % 26
            result_char = chr(97 + index)
            if not is_upper:
                result += result_char
            else:
                result += result_char.upper()
        else:
            result += char
        
    return result

print encrypt(encrypt_str, k)