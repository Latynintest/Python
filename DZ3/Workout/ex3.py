from student import Student
from cource import CourseGroup

student1 = Student('Sergey', 'Latynin', 38, 5)
student2 = Student('Elena', 'Zhirnova', 45, 5)
student3 = Student('Alexey', 'Pavlov', 35, 5)
student4 = Student('Anatoly', 'Lung', 30, 5)
student5 = Student('Igor', 'Vorobyov', 32, 5)
classmates = [student2, student3, student4, student5]

group = CourseGroup(student1, classmates)
print(group)
