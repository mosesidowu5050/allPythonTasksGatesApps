from facilitators import Instructor
from students import Student


def register_user(role, name, email, password, file_path="users.txt"):
    try:
        with open(file_path, "r") as file:
            for line in file:
                if email in line:
                    raise ValueError("Email already registered.")
    except FileNotFoundError:
        pass

    with open(file_path, "a") as file:
        file.write(f"{role}|{name}|{email}|{password}\n")
    if role == "student":
        return Student(name, email, password)
    else:
        return Instructor(name, email, password)


def login(email, password, file_path="users.txt"):
    try:
        with open(file_path, "r") as file:
            for login_line in file:
                parts = login_line.strip().split("|")
                if parts[2] == email and parts[3] == password:
                    if parts[0] == "student":
                        courses = {}
                        if len(parts) > 4:
                            for entry in parts[4].split(","):
                                if ":" in entry:
                                    course, grade = entry.split(":")
                                    courses[course] = grade
                        return Student(parts[1], parts[2], parts[3], courses)
                    else:
                        return Instructor(parts[1], parts[2], parts[3])
    except FileNotFoundError:
        print("users.txt not found")

    return None
