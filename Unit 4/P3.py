# Design and implement a program with class student having two methods with name set () but accepts different number of arguments. Include necessary methods to display the student details.

class student:
    def __init__(self, name, usn, grade):
        self.name = name
        self.usn = usn
        self.grade = grade
    def set(self, name_correct, usn_permanent):
        self.name = name_correct
        self.usn = usn_permanent
    def set(self, grade):
        self.grade = grade
    def print(self):
        print("Student Name: ", self.name)
        print("USN: ", self.usn)
        print("Grade: ", self.grade)
        print("\n")

stud1 = student("XYZ", "1MS20ECXXX", 69)
stud2 = student("ABC", "1MS20ECXXX")
stud1.print()
stud2.print()