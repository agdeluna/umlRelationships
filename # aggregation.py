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

