#!/usr/bin/python3
"""Daclares a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a square

            Args:
                size: size of square
                
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
