#!/usr/bin/python3
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # Validate width and height using inherited method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Assign private attributes
        self.__width = width
        self.__height = height
