s = input().strip()

original_message = list('SOS')
message_length = len(original_message)

altered_char_count = 0

for i, char in enumerate(s):
    message_index = i % message_length
    if char != original_message[message_index]:
        altered_char_count += 1

print(altered_char_count)
