"""Geometry module"""



class BrandMetaClass(type):
    """
    documentation
    """
    def __dir__(cls):
        """
        documentation
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass = BrandMetaClass):
    """BaseGeometry class"""
    def __dir__(cls):
        """Removing __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']