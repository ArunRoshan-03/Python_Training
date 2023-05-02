# Jumping Statement

# Reversed the String value.
print("Print the Student name")
Student_Name = ["Arun", "roshan", "kutty", None, "Jack"]
print(len(Student_Name))  # who to find the length
Name_List: str | None
for Name_List in Student_Name:
    if Name_List is not None:
        break
    print("the Student name : {0}".format(Name_List))
