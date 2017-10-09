import re

CHARACTERS_BETWEEN_ALPHA_RE = re.compile(r'(?<=\w)\W+(?=\w)')

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0

for i_matrix in range(n):
    matrix_t = list(input()) + [''] * m
    matrix.append(matrix_t)

result_str = ''

for j in range(m):
    result_str += ''.join(
        [
            matrix[i][j]
            for i
            in range(n)
        ]
    )

print(CHARACTERS_BETWEEN_ALPHA_RE.sub(' ', result_str))
