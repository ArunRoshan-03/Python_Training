# *Args
def sum(*args):
    input = 0
    for value in args:
        input += value
    print(input)


sum(1, 3, 4)


# *args with pass with in parameter
def sum(a, b, c):
    print(a, b, c)


sum_value = [1, 4, 10]

sum(*sum_value)

# * args with lambda function
result = lambda a, b, c: a + b * c

sum_value = [1, 4, 10]
print(result(*sum_value))


# ** Kwargs
def student_list(**kwargs):
    for Key, Value in kwargs.items():
        print(Key, ":", Value)


student_detail = {
    "Class A": {
        "Student_Id": 134,
        "Student_Name": "Arun",
        "Student_Sec": "D",
        "Student_Std": 12
    },
    "Class B": {
        "Student_Id": 194,
        "Student_Name": "Roshan",
        "Student_Sec": "E",
        "Student_Std": 12
    }
}

student_list(**student_detail)
