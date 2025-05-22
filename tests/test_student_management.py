import unittest
import os

from student_management import register_user, login
from students import Student
from facilitators import Instructor

TEST_FILE = "test_users.txt"

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        with open(TEST_FILE, "w") as file:
            pass

    def test_clean_up_file_after_each_testing(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)


    def test_view_courses_returns_correct_course_list(self):
        courses = {
            "Mathematics": "A",
            "English": "B"
        }
        student = Student("John Doe", "john@example.com", "securepass", courses)
        course_list = list(student.view_courses())

        self.assertIn(("Mathematics", "A"), course_list)
        self.assertIn(("English", "B"), course_list)
        self.assertEqual(len(course_list), 2)

    def test_view_courses_returns_empty_when_no_courses(self):
        student = Student("Jane Smith", "jane@example.com", "pass123")
        course_list = list(student.view_courses())
        self.assertEqual(len(course_list), 0)



    def test_instructor_can_create_course(self):
        instructor = Instructor("Dr. Eric", "eric@semicolon.edu", "pass123")
        course_name = "IntroToPython"
        instructor.create_course(course_name)

    def test_instructor_can_assign_grade_to_student(self):
        instructor = Instructor("Dr. Eric", "eric@semicolon.edu", "pass123")
        student_email = "bode@semicolon.com"
        with open("users.txt", "w") as file:
            file.write(f"student|Bode Bode|{student_email}|pass123\n")
        instructor.assign_grade("DataStructures", student_email, "A")



    def test_register_student_successfully(self):
        student = register_user("student", "Moses Idowu", "moses@gmail.com", "pass1234", file_path=TEST_FILE)
        self.assertIsInstance(student, Student)
        self.assertEqual(student.email, "moses@gmail.com")

    def test_register_duplicate_email_raises_error(self):
        register_user("student", "Moses Idowu", "moses@gmail.com", "pass1234", file_path=TEST_FILE)
        with self.assertRaises(ValueError) as context:
            register_user("student", "Idowu Moses", "moses@gmail.com", "pass2222", file_path=TEST_FILE)
        self.assertEqual(str(context.exception), "Email already registered.")

    def test_login_successful_for_student(self):
        register_user("student", "Yusuf", "yusuf@yahoo.com", "pass1234", file_path=TEST_FILE)
        user = login("yusuf@yahoo.com", "pass1234", file_path=TEST_FILE)
        self.assertIsInstance(user, Student)
        self.assertEqual(user.name, "Yusuf")

    def test_login_invalid_credentials_returns_none(self):
        register_user("student", "Majek", "majek@onijogbon.com", "pass1234", file_path=TEST_FILE)
        user = login("majek@onijogbon.com", "wrongpass", file_path=TEST_FILE)
        self.assertIsNone(user)




if __name__ == "__main__":
    unittest.main()
