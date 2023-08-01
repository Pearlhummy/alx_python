"""
this is class

"""


class Square:
    """
    class Square that defines a square

    """

    def __init__(self, size=0):
        """
        Instantiation with size (no type/value verification)

        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")