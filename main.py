# main.py

from student import Student
from teacher import Teacher

# Bir öğrenci ve bir öğretmen örneği oluşturun
student = Student("Ali", 20, "S12345")
teacher = Teacher("Ayşe", 35, "Mathematics")

# Bilgileri görüntüleyin
print("Student Information:")
student.display_info()

print("\nTeacher Information:")
teacher.display_info()
