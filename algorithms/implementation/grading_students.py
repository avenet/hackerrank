#!/bin/python3


def compute_grade(grade):
    if grade < 38:
        return grade
    
    difference = 5 - (grade % 5)
    
    if difference < 3:
        return difference + grade
    
    return grade


def solve(grade_values):
    return [
        compute_grade(grade)
        for grade
        in grade_values
    ]


n = int(input().strip())

grades = []
grades_i = 0

for _ in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)

result = solve(grades)

print("\n".join(map(str, result)))
