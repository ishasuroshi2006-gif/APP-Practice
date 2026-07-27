class Student:
    college = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    @staticmethod
    def message():
        print("Welcome to Python Programming")

s1 = Student("Isha", 90)

s1.display()
Student.show_college()
Student.message()
