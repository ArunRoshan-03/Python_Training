Emp_Name = 'kumar'
Emp_Id = 1230
Emp_Salary = 25.344

# Approach1
print("By printing all the values")
print(Emp_Name, Emp_Salary, Emp_Id)

# Approach2
print("By printing normal output way")
print("Employee name is:", Emp_Name)
print("Employee Id is:", Emp_Id)
print("Employee Salary is:", Emp_Salary)

# Approach3
print("By using % formatting output way ")
print("Employee name is: %s " % Emp_Name)
print("Employee Id is: %d" % Emp_Id)
print("Employee Salary is:%f" % Emp_Salary)

# Approach 4
print("By using {} Formatting output way")
print("Employee Name is:{}".format(Emp_Name))
print("Employee Id is:{}".format(Emp_Id))
print("Employee Salary is:{}".format(Emp_Salary))

# Approach5
print("By using {} and index value to Formatting output way")
print("Employee Name is:{1}, Employee Id is:{2} ,Employee Salary is:{0}".format(Emp_Salary, Emp_Name, Emp_Id))
