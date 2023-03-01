number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    grades_string = " ".join(map(lambda grade: f"{grade:.2f}", grades))
    print(f"{name} -> {grades_string} (avg: {average_grade:.2f})")
