class Error():
    """Class for storing error/warning definitions
    """
    def __init__(self, code: str, name: str):
        """
        Args:
            code (str):     code of the error/warning encountered
            name (str):     name of the error/warning encountered
        """
        self.code = code
        self.name = name

    def what_short(self, line: int) -> str:
        """Function generating a short description of the error/warning.

        Args:
            line (int):     line at which the error/warning was encountered.
        """
        return self.code + " " + self.name + " at line " + str(line) + "."

    """Function (lambda in fact) generating a verbose description of the error/warning.
    By default it returns the short description with an information that no verbose version was defined.

    Args:
        line (int):     line at which the error/warning was encountered.
        args ([str]):   list of additional arguments used to produce the verbose error description
                            e.g. macro name
    """
    what_long = lambda self, line, args: self.what_short(line) + " No verbose version defined."