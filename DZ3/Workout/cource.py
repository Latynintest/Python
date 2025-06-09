class CourseGroup:
    def __init__(self, student, classmates):
        self.student = student
        self.classmates = classmates

    def __str__(self):
        classmates_str = ""
        for classmate in self.classmates:
            if classmate != self.student:
                if classmates_str:
                    classmates_str += ", "
                classmates_str += str(classmate)
        return f"{self.student} вместе с: {classmates_str}"
