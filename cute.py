import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector2D({self.x:.2f}, {self.y:.2f})"


v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(f"Vector 1: {v1}")
print(f"Magnitude of v1: {v1.magnitude()}")
print(f"Normalized v1: {v1.normalize()}")
print(f"Dot Product (v1 . v2): {v1.dot(v2)}")
print(f"Sum (v1 + v2): {v1.add(v2)}")