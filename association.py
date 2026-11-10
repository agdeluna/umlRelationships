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

