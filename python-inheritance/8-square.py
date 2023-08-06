"""Square module"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)

        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        return self.__size * self.__size