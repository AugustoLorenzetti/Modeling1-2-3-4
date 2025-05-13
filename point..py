import random

class Point:
    """
    A class to represent a point in 2D Cartesian coordinates.

    Attributes:
    -----------
    x : float or int
        The x-coordinate of the point.
    y : float or int
        The y-coordinate of the point.
    """

    def __init__(self, x, y):
        """
        Initialize a Point object.

        Parameters:
        -----------
        x : float or int
            The x-coordinate on the axis.
        y : float or int
            The y-coordinate on the axis.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a user-friendly string representation of the Point instance.

        Returns:
        --------
        str
            A string in the form 'point<x,y>'.
        """
        return f"point<{self.x},{self.y}>"

    def __repr__(self):
        """
        Return an unambiguous string representation for debugging.

        Returns:
        --------
        str
            A string in the form '<x,y>'.
        """
        return f"<{self.x},{self.y}>"

    def distance_orig(self):
        """
        Calculate the Euclidean distance of the point from the origin (0, 0).

        Returns:
        --------
        float
            The distance from the origin.
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Override the '>' operator to compare two points based on their distance from the origin.

        Parameters:
        -----------
        other : Point
            Another Point instance to compare with.

        Returns:
        --------
        bool
            True if self is farther from the origin than other.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def __eq__(self, other):
        """
        Override the '==' operator to check equality based on distance from the origin.

        Parameters:
        -----------
        other : Point
            Another Point instance to compare with.

        Returns:
        --------
        bool
            True if both points are at the same distance from the origin.
        """
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance


# --- Example Usage ---

p = Point(1, 2)
p2 = Point(2, 3)
p4 = Point(4.4, -55)

print(f"p.x = {p.x} and p.y = {p.y}")
print(f"p4.x = {p4.x} and p4.y = {p4.y}")

p.x = 20
print(f"After modifying p.x, p.x = {p.x} and p.y = {p.y}")
print(p)

# Create a list of 5 random points
points = []
for i in range(5):
    points.append(Point(random.randint(-10, 10),  # x value
                        random.randint(-10, 10))) # y value

print("I got these 5 random points:")
print(points)

p = Point(3, 4)
print(p.distance_orig())  # Expected output: 5.0

p2 = Point(1, 1)
print(f"I am comparing p > p2: {p > p2}")  # Expected output: True

print("The sorted list of points is:")
points.sort()
print(points)



