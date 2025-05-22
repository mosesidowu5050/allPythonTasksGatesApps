from user import User

class Instructor(User):
    def __init__(self, name, email, password):
        super().__init__('instructor', name, email, password)

    def create_course(self, course_name):
        with open("courses.txt", "a") as file:
            file.write(f"{course_name}|{self.email}\n")


    def assign_grade (self, course_name, student_email, grade):
        grade_update = []
        found = False
        try:
            with open ("users.txt", "r") as file:
                for all_grades in file:
                    parts = all_grades.strip().split("|")
                    if parts[0] == "student" and parts[2] == student_email:
                        found = True
                        courses = {}
                        if len(parts) > 4 and parts[4]:
                            for entry in parts[4].split(","):
                                if ":" in entry:
                                    course_name, course_grade = entry.split(":")
                                    courses[course_name] = course_grade
                        courses[course_name] = grade
                        course_to_string = ",".join(f"{key}:{value}" for key, value in courses.items())
                        grade_update.append(f"student|{parts[1]}|{parts[2]}|{parts[3]}|{course_to_string}\n")
                    else:
                        grade_update.append(all_grades)
        except FileNotFoundError:
            print("users.txt not found")

