import re
from student_management import register_user, login

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_name(name):
    return re.match(r"^[A-Za-z\s]+$", name)

def is_valid_password(password):
    return len(password) >= 6


def student_menu(student):
    while True:
        print(f"\nWelcome, {student.name} (Student)")
        print("1. View My Courses and Grades")
        print("2. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            courses = student.view_courses()
            if courses:
                for course, grade in courses:
                    print(f"Course: {course} | Grade: {grade}")
            else:
                print("You are not enrolled in any courses yet.")
        elif choice == "2":
            break
        else:
            print("Invalid option. Try again.")


def instructor_menu(instructor):
    while True:
        print(f"\nWelcome, {instructor.name} (Instructor)")
        print("1. Create Course")
        print("2. Assign Grade to Student")
        print("3. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            course_name = input("Enter course name to create: ")
            instructor.create_course(course_name)
            print("Course created.")
        elif choice == "2":
            course_name = input("Enter course name: ")
            student_email = input("Enter student email: ")
            grade = input("Enter grade to assign: ")
            instructor.assign_grade(course_name, student_email, grade)
            print("Grade assigned.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")

def main_menu():
    while True:
        print("\n=== Course Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                role = input("Enter role (student/instructor): ").lower()
                while role not in ["student", "instructor"]:
                    role = input("Invalid input. Enter role (student/instructor): ").lower()

                name = input("Enter your name: ")
                while not is_valid_name(name):
                    name = input("Invalid name. Please use only letters and spaces: ")

                email = input("Enter email: ")
                while not is_valid_email(email):
                    email = input("Invalid email. Enter a valid email (e.g., name@example.com): ")

                password = input("Enter password (min 6 characters): ")
                while not is_valid_password(password):
                    password = input("Password too short. Enter at least 6 characters: ")

                user = register_user(role, name, email, password)
                print("Registration successful.")

            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = login(email, password)
            if user:
                if user.role == "student":
                    student_menu(user)
                else:
                    instructor_menu(user)
            else:
                print("Invalid credentials.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main_menu()