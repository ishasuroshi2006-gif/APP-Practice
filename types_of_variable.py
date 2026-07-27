college = "MIT ADT"

class Student:
    
    def __init__(self, name):
        
        self.name = name

    def display(self):
        
        course = "BTech CSE"

        print("Global Variable (College):", college)
        print("Instance Variable (Name):", self.name)
        print("Local Variable (Course):", course)

s1 = Student("Isha")
s1.display()
