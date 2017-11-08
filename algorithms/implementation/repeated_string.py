s = input().strip()
n = int(input().strip())

a_count = s.count('a')
whole_str_reps = n // len(s)

partial_str_length = n % len(s)
partial_str = s[:partial_str_length]
partial_str_a_count = partial_str.count('a')

print(a_count * whole_str_reps + partial_str_a_count)
