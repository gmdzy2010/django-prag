"""
This file contain all of the exceptions occurring during rendering the html
templates to pdf file
"""

class MethodIllegalException(Exception):
    """Method illegal exception"""
    pass


class ContextEmptyException(Exception):
    """The context data rendered into the template must not be empty, or will
     raise this exception.
     """
    pass
