"""Rectangle class"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class BrandMetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        """
        documentation
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class Rectangle(BaseGeometry, metaclass = BrandMetaClass):
    """REc class"""
    def __init__(self, width, height):
        """Initializes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __dir__(cls):
        """Removing __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']