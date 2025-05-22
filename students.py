from user import User

class Student(User):
    def __init__(self, name, email, password, courses=None):
        super().__init__('student', name, email, password)
        self.courses = courses if courses else {}

    def view_courses(self):
        return self.courses.items()
