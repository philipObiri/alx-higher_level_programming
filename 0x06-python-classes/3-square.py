#!/usr/bin/python3
"""Define class Square"""

class Square:
    """Represents a square

    Attributes:
        __sizesize of a side of the square
    """
    def __init__(self, size=0):
        """initialize the square

        Args:
            size (ize of a side of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size m be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculate the square's area

        Returns:
            The area of the square (in value)
        """
        return (self.__size) ** 2
