# inheritance.py

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal): # Generalization / Inheritance
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} is barking.")

if __name__ == "__main__":
    my_dog = Dog("Buddy")
    my_dog.eat()
    my_dog.bark()

