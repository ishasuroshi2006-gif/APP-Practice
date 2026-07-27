class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def animal_sound(animal):
    animal.sound()

c = Cat()
d = Dog()

animal_sound(c)
animal_sound(d)
