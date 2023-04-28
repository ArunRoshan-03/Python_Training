# Simple Function
def sum(Max_Number, Min_number):
    result = 0
    for value in range(Max_Number, Min_number + 1):
        result = result + value
    return result


Values = sum(10, 20)
print(Values)


def verify_student_name(student_name):
    # Check if the student name is valid
    if len(student_name) < 3:
        return "Invalid student name: name should be at least 3 characters long."
    elif not student_name.isalpha():
        return "Invalid student name: name should only contain alphabetic characters."
    else:
        return "Valid student name: {}.".format(student_name)


S = verify_student_name("un")
print(S)


# Argument with default values(positional)
def passing_values(i, j=13):
    if i >= j:
        print({i}, "is greater than", {j})
    else:
        print({i}, "is lesser than", {j})


passing_values(23)


# keyword and positional arguments type
def Emp_detail(Id, Name):
    print("Employee Name is :", Name, "Employee Id is :", Id)


Emp_detail(12, 'Arun')  # Positional Arguments
Emp_detail(Id=23, Name="Kutty")  # Keyword Arguments


# Multiple return type
def sum(Value1, Value2):
    if Value1 > Value2:
        return Value1, Value2
    else:
        return Value2, Value1

result = sum(12,89)
print(result)