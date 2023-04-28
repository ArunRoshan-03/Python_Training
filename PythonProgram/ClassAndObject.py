# creating basic class and object which include method
student_name = "Kanna"
student_id = 8839

class ClassAndObject:
    student_name = "Ram"
    student_id = 1234

    def Student_id(self):
        pass

    # Declaring variables inside the class
    def Student_Name(self):
        if self.student_name is not None:
            print("Student Name is not none %s" % self.student_name)
        else:
            print("Student Mane is none")

    # Instance method and static method and passing parameter.
    @staticmethod
    def Student_Sec(Id):
        if Id == None:
            print("your", {Id}, "is enter Successfully")
        else:
            print({Id}, "is Integer value")

    def Student_details(self, student_name, student_id):
        print("Enter the student detail with local variable:", student_name, student_id)
        print("Enter the student detail with Class variable:", self.student_name, self.student_id)
        print("Enter the student detail with Global variable:", globals()['student_name'], globals()['student_id'])


classAndObject = ClassAndObject()
classAndObject.Student_id()
ClassAndObject.Student_Sec("123")
classAndObject.Student_Name()

# Name less object
ClassAndObject().Student_details("Arel", 980)
