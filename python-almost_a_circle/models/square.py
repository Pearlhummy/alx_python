"""Module rectangle documentatin"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        """methode documentation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method ."""
        return "[Square] ({id}) {x}/{y} - {size}".format(
            id=self.id,
            x=self.x, y=self.y,
            size=self.width
        )
    @property
    def size(self):
        """adding the public getter 
        and setter size
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value