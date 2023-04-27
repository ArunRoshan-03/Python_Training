# For Loop
# iterative the number 0 to 20 by using for loop
print("iterative the number")
for number in range(21):
    print(number)

# Reverse the number 20 to 0 by using for loop
print("reverse the number")
for number in range(20, -1, -1):
    print("Reverse from 20 to o number is %d" % number)

# pick odd the number 20 by using for loop
print("odd the number")
for number in range(1, 20, 2):
    print("odd the number is :{}".format(number))

# pick even the number 20 by using for loop
print("Even the number")
for number in range(2, 20, 2):
    print("Even the number is : {0}".format(number))

# iterative the String value.
print("Print the Student name")
Student_Name = ["Arun", "roshan", "kutty", "Jack"]
for Name_List in Student_Name:
    print(Name_List)

# Reversed the String value.
print("Print the Student name")
Student_Name = ["Arun", "roshan", "kutty", "Jack"]
print(len(Student_Name))  # who to find the lengh
for Name_List in reversed(Student_Name):
    print("Reversed  the Student name : {0}".format(Name_List))

