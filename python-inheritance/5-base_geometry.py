"""Geometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area methode"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator methode"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __dir__(cls) -> None:
        attributes=super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']