class University:
    def print_info(self):
        print("Університет")


class Faculty(University):
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Факультет:", self.name)


class Department(Faculty):
    def __init__(self, faculty_name, department_name):
        super().__init__(faculty_name)
        self.department_name = department_name

    def print_info(self):
        print("Кафедра:", self.department_name)


objects = [
    University(),
    Faculty("Інформатика"),
    Department("Інформатика", "Програмна інженерія")
]

for obj in objects:
    obj.print_info()
