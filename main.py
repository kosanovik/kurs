# Кортеж (tuple, immutable) не изменямый список
# Студент и средний бал

N=3
students = []
for _ in range(N):
    student, averge = input("ФИО: "), float(input("Ср. бал: "))
    students.append((student, averge))
    
print(students)

for st in students:
    student, averge = st
    print("Студент: ", student)
    print("Средний бал: ", averge)