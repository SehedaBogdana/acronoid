import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):  # довжина вектора
        return math.sqrt(self.x ** 2 + self.y ** 2)
        # sqrt це корінь

    def __add__(self, other):  # ще одна можливість створити службову функцію
     #  яка дозволить використовувати не просто як метод add а писати просто плюс
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

