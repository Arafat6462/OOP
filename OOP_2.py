class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

class Dog(Pet):
    def speak(self):
        print("Woof Woof!")

class Cat(Pet):
    def speak(self):
        print("Meow Meow!")

p = Pet("Buddy", 5)
p.show()
cat = Cat("Kitty", 3)
cat.show()
cat.speak()
dog = Dog("Tommy", 4)
dog.show()
dog.speak()