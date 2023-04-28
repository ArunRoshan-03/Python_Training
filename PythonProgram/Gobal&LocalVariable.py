# Gobal variable And local variable with function method

Student_name = "Arun"


def student_name():
    global  Student_name
    Student_name ="kutty"
    if Student_name is not None:
        return "Student Name is not None", {Student_name}
    else:
        return "Student name is None"


s = student_name()
print(s)
