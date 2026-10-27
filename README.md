# umlRelationships
# association.py

class Professor:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, head_professor):
        self.dept_name = dept_name
        self.head_of_department = head_professor # Association

    def display_info(self):
        print(f"Department: {self.dept_name}, Head: {self.head_of_department.name}")

if __name__ == "__main__":
    prof = Professor("Dr. Smith")
    dept = Department("Computer Science", prof)
    dept.display_info()




# composition.py

class House:
    class _Room: # Inner class representing part of the house
        def __init__(self, room_type):
            self.room_type = room_type

    def __init__(self, address, room_type):
        self.address = address
        self.bedroom = self._Room(room_type) # Composition (Lifecycle is tied to House)

    def display_house(self):
        print(f"House at {self.address} contains a {self.bedroom.room_type}.")

if __name__ == "__main__":
    house = House("123 Main St", "Master Bedroom")
    house.display_house()


# aggregation.py

class Student:
    def __init__(self, name):
        self.name = name

class Classroom:
    def __init__(self, room_number, students):
        self.room_number = room_number
        self.students = students # Aggregation (Students can exist independently)

    def show_classroom(self):
        print(f"Classroom {self.room_number} has students:")
        for student in self.students:
            print(f"- {student.name}")

if __name__ == "__main__":
    student_list = [Student("Alice"), Student("Bob")]
    room = Classroom("101", student_list)
    room.show_classroom()



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



# dependency.py

class Fuel:
    def burn(self):
        print("Fuel is burning, energy released.")

class Car:
    def start(self, fuel): # Dependency (Car uses Fuel temporarily in a method)
        fuel.burn()
        print("Car has started.")

if __name__ == "__main__":
    car = Car()
    fuel = Fuel()
    car.start(fuel)
