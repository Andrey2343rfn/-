from typing import Generic, TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2")

class Pair(Generic[T1, T2]):
    def __init__(self, first: T1, second: T2):
        self.first = first
        self.second = second

    def get_first(self) -> T1:
        return self.first

    def get_second(self) -> T2:
        return self.second

    def __str__(self):
        return f"{self.first}, {self.second}"


# Приклад використання
p1: Pair[int, float] = Pair(5, 3.14)
p2: Pair[str, int] = Pair("A", 10)

print(p1)
print(p2)
