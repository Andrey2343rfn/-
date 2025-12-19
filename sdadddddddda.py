import math

class SolidOfRevolution:
    def volume(self):
        return 0

    def print_info(self):
        print("Фігура обертання")


class Cone(SolidOfRevolution):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height / 3

    def print_info(self):
        print("Конус")
        print("Радіус:", self.radius)
        print("Висота:", self.height)
        print("Обʼєм:", self.volume())


objects = [
    SolidOfRevolution(),
    Cone(3, 5),
    Cone(2, 4)
]

for obj in objects:
    obj.print_info()
    print()
