class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines what is printed when you call str(Vector) or print(Vector)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Overrides the '+' operator
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add two Vectors together")
        return Vector(self.x + other.x, self.y + other.y)

    # Overrides the '==' operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 4)
v2 = Vector(3, 1)

print(f"Addition: {v1} + {v2} = {v1 + v2}")
print(f"Equality Check: {v1 == Vector(2, 4)}")