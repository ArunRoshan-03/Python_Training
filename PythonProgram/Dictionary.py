# Student list

Student_details = {
    "Student1": {
        "id": "123",
        "student_Name": "Arun",
        "student_Std": "B"
    },
    "student2": {
        "id": "423",
        "student_Name": "dsd",
        "student_Std": "B"
    }
}

# Retrieving the element
print(Student_details["Student1"]["student_Name"])
print(Student_details["student2"]["student_Std"])

# Addeding the element
Student_details["Student1"]["student_Sec"] = 10
Student_details["student2"]["student_Sec"] = 12
print(Student_details)

# modified the element
Student_details["Student1"]["student_Sec"] = 11
Student_details["student2"]["student_Sec"] = 1
print(Student_details)

# Deleting the elemnts
del Student_details["student_Sec"]
print(Student_details)


trim_Value =str(Student_details).replace("},", " }")
print(trim_Value)
print(len(Student_details))

# for loop in dictionary
for student_info, key in Student_details.items():
    print("Student_batch:", student_info)
    print("ID:", Student_details[student_info]["id"])
    print("ID:", Student_details[student_info]["student_Name"])
    print("ID:", Student_details[student_info]["student_Std"])
    print()

for student_info in Student_details:
    print(student_info, ":", Student_details[student_info])

print("\n", len(Student_details.items()))

# Student_details["Student1"].popitem()
# print(Student_details)

if Student_details["Student1"].values() == Student_details["student2"].values():
    print("Both value are same")
else:
    mismatch = {}
    for value in Student_details["Student1"]:
        if Student_details["Student1"][value] != Student_details["student2"][value]:
            mismatch[value] = (Student_details["Student1"][value], Student_details["student2"][value])
        print("Mismatched", mismatch)

    print("Both values or not same")
