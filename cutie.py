import math


class Vector2D:

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vector2D(self.x * scalar, self.y * scalar)

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print("v1:", v1)
print("v1 + v2:", v1 + v2)
print("v1 * 3:", v1 * 3)
print("Dot Product:", v1.dot(v2))
print("v1 Magnitude:", v1.magnitude())
print("v1 Normalized:", v1.normalize())