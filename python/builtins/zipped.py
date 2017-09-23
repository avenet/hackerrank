m, n = map(int, input().split())

all_marks = list()

for i in range(n):
    all_marks.append(
        map(
            float,
            input().split()
        )
    )

for student_marks in zip(*all_marks):
    student_average = sum(student_marks) / len(student_marks)
    
    print(round(student_average, 1))
