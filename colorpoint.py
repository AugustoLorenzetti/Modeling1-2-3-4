from point import Point
import random

class PointException(Exception):
    """Custom exception class for Point-related errors."""
    pass

class ColorPoint(Point):
    """
    A subclass of Point that adds color as an attribute.

    Inherits from:
    ---------------
    Point : Base class representing a 2D point.

    Attributes:
    -----------
    x : float or int
        The x-coordinate of the point.
    y : float or int
        The y-coordinate of the point.
    color : str
        A string representing the color of the point.
    """

    def __init__(self, x, y, color):
        """
        Initialize a ColorPoint object.

        Parameters:
        -----------
        x : float or int
            The x-coordinate.
        y : float or int
            The y-coordinate.
        color : str
            The color label for the point.

        Raises:
        -------
        TypeError:
            If x or y are not numeric types.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        super().__init__(x, y)  # Call parent constructor
        self.color = color

    def __str__(self):
        """
        Return a user-friendly string showing color and coordinates.

        Returns:
        --------
        str
            A string in the format '<color: x, y>'.
        """
        return f"<{self.color}: {self.x}, {self.y}>"


# --- Main block: test functionality ---

if __name__ == "__main__":
    # Create and display a sample ColorPoint
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())  # Expected: ~2.236
    print(p)

    # Example block to generate, sort, and display random ColorPoints
    colors = ["red", "green", "blue", "yellow", "black"]
    color_points = []
    for i in range(10):
        color_points.append(
            ColorPoint(random.randint(-10, 10),
                       random.randint(-10, 10),
                       random.choice(colors))
        )

    print("List of random ColorPoints:")
    print(color_points)

    # Sort by distance from origin (uses Point.__gt__)
    color_points.sort()
    print("Sorted ColorPoints:")
    print(color_points)
