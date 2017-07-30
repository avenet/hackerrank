input_str = raw_input()

occurrences = []
current_char = None
current_ocurrences = None

for char in input_str:
    if not current_char and not current_ocurrences:
        current_char = char
        current_ocurrences = 1
    elif current_char == char:
        current_ocurrences += 1
    else:
        occurrences.append(str((current_ocurrences, (int(current_char)))))
        current_char = char
        current_ocurrences = 1
        
occurrences.append(str((current_ocurrences, (int(current_char)))))
    
print ' '.join(occurrences)