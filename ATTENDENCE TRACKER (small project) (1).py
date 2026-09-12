# ATTENDENCE TRACKER
class Student:
    def present_or_absent(self):
        student_status  = input(f"{self.name} is : ")
        print(student_status)
        
s1  = Student()
s2  = Student()
s3  = Student()
s1.name = "Albert Einstein"
s2.name = "Stephan Hawking"
s3.name = "Issac Newton"
s1.present_or_absent()

s2.present_or_absent()

s3.present_or_absent()



