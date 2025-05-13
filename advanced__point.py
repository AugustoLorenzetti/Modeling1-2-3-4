from color_point import ColorPoint, PointException

class AdvancedPoint(ColorPoint):
    """
    A subclass of ColorPoint that introduces property methods,
    color validation, class-level color extension, and static utilities.

    Attributes:
    -----------
    _x : float or int
        The x-coordinate (private).
    _y : float or int
        The y-coordinate (private).
    _color : str
        The color of the point.

    Class Attributes:
    -----------------
    COLORS : list of str
        A list of allowed color names.
    """

    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]

    def __init__(self, x, y, color):
        """
        Initialize an AdvancedPoint object with strict color checking.

        Parameters:
        -----------
        x : float or int
            The x-coordinate.
        y : float or int
            The y-coordinate.
        color : str
            A color label from the allowed COLORS list.

        Raises:
        -------
        TypeError
            If the color is not in the allowed COLORS list.
        """
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}")
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """Getter method for x-coordinate."""
        return self._x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate."""
        self._x = value

    @property
    def y(self):
        """Getter method for y-coordinate."""
        return self._y

    @property
    def color(self):
        """Getter method for color."""
        return self._color

    @classmethod
    def add_color(cls, color):
        """
        Add a new color to the class-level allowed COLORS list.

        Parameters:
        -----------
        color : str
            The color to be added.
        """
        cls.COLORS.append(color)

    @staticmethod
    def from_tuple(coordinate, color="red"):
        """
        Create a new AdvancedPoint from a tuple input.

        Parameters:
        -----------
        coordinate : tuple of (float, float)
            A 2D coordinate pair (x, y).
        color : str, optional
            Color label for the new point. Defaults to "red".

        Returns:
        --------
        AdvancedPoint
            A new instance of AdvancedPoint.
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculate Euclidean distance between two AdvancedPoint instances.

        Parameters:
        -----------
        p1, p2 : AdvancedPoint
            Two points to compute distance between.

        Returns:
        --------
        float
            Euclidean distance.
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def distance_to_other(self, p):
        """
        Calculate distance from self to another point.

        Parameters:
        -----------
        p : AdvancedPoint
            Another point instance.

        Returns:
        --------
        float
            Euclidean distance between self and p.
        """
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5


# --- Example Usage ---

AdvancedPoint.add_color("rojo")  # Extend allowed colors

p = AdvancedPoint(1, 2, "blue")
print(p.x)                    # Should print 1
print(p)                      # Inherits __str__ from ColorPoint
print(p.distance_orig())      # Distance from origin

p2 = AdvancedPoint.from_tuple((3, 2))  # Create from tuple with default color
print(p2)

# Compute distances
print(AdvancedPoint.distance_2_points(p, p2))  # Static method call
print(p.distance_to_other(p2))                 # Instance method call
