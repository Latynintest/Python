class Student:
    def __init__(self, name, last_name, age, course):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.course = course

    def __str__(self):
        return f'{self.name} {self.last_name}, {self.age} лет, учиться на курсе {self.course}'
