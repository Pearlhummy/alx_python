"""
fonction that check instance of a class

"""


def inherits_from(obj, a_class):

    """checks  the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj (Any): The object to check
        a_class (Any): The class to check against

    Returns:
        bool: The check result
    """

    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False