str_value = input()

current_character = None
current_repetitions = 0

repetitions_list = []

for char in str_value:
    if current_character != char:
        if current_character is not None:
            current_char_info = (
                current_repetitions,
                int(current_character)
            )
            
            repetitions_list.append(
                current_char_info
            )
        
        current_character = char
        current_repetitions = 1
    else:
        current_repetitions += 1

if current_character and current_repetitions:
    current_char_info = (
        current_repetitions,
        int(current_character)
    )
    
    repetitions_list.append(
        current_char_info
    )

print(
    ' '.join(
        map(
            str,
            repetitions_list
        )
    )
)
