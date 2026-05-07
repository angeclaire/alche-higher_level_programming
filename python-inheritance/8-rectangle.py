#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The private width of the rectangle.
        __height (int): The private height of the rectangle.
    """

    def __init__(self, width, height):
        """Instantiate a Rectangle with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
