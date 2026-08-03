class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

class AnimalFactory:
    def get_animal(self, animal):
        if animal == "dog":
            return Dog()
        elif animal == "cat":
            return Cat()
        else:
            return None

factory = AnimalFactory()

animal = factory.get_animal("dog")
print(animal.sound())

animal = factory.get_animal("cat")
print(animal.sound())
