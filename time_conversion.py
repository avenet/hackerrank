time_parts = raw_input().split(':')

if time_parts[-1].endswith('PM'):
    time_parts[-1] = time_parts[-1].replace('PM', '')
    if time_parts[0] != '12':
        time_parts[0] = str(int(time_parts[0]) + 12)
else:
    time_parts[-1] = time_parts[-1].replace('AM', '')
    if time_parts[0] == '12':
        time_parts[0] = '00'

print ':'.join(time_parts)