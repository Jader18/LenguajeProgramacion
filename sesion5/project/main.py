from classes import Student

student1 = Student(1, "Jader", "ISI")
student2 = Student(2, "Maria", "Derecho")
student3 = Student(3, "Marco", "ISI")


students = []
students.append(student1)
students.append(student2)
students.append(student3)

#mostras lista
for stu in students: 
    print(stu)
