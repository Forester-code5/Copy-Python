# Task1. Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.
import math


class Polygon:
    """
    A class to represent a generic polygon.

    Attributes:
    ----------
    num_sides : int
        Number of sides of the polygon.
    side_lengths : list
        List to store the lengths of each side.
    """

    def __init__(self, num_sides):
        """Initializes a Polygon with the specified number of sides."""
        if num_sides < 3:
            raise ValueError("A polygon must have at least 3 sides.")
        self.num_sides = num_sides
        self.side_lengths = [0] * num_sides

    def set_side_length(self, side_index, length):
        """Sets the length of a specific side of the polygon."""
        if side_index < 0 or side_index >= self.num_sides:
            raise IndexError("Invalid side index.")
        if length <= 0:
            raise ValueError("Side length must be positive.")
        self.side_lengths[side_index] = length

    def get_side_length(self, side_index):
        """Returns the length of a specific side."""
        if side_index < 0 or side_index >= self.num_sides:
            raise IndexError("Invalid side index.")
        return self.side_lengths[side_index]

    def perimeter(self):
        return sum(self.side_lengths)

    def area(self):
        """Calculates and returns the area of a regular polygon."""
        if len(set(self.side_lengths)) > 1:
            raise ValueError("The polygon is not regular. Area calculation requires all sides to be equal.")
        side_length = self.side_lengths[0]
        n = self.num_sides
        return (n * side_length ** 2) / (4 * math.tan(math.pi / n))


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 10)
print(f"The area of the rectangle is: {rectangle.area()}")
