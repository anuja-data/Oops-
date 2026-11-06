class Student:
    college = "IMCC"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", Student.college)

s1 = Student("Anuja")
s1.display()