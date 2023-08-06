"""Geometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area methode"""
        raise Exception("area() is not implemented")

    def __dir__(cls) -> None:
        attributes=super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']