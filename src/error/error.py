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
        self.verbose = lambda args: "No verbose version defined."

    def what_short(self, line: int) -> str:
        """Function generating a short description of the error/warning.

        Args:
            line (int):     line at which the error/warning was encountered.
        """
        if line == None:
            t = ""
        else:
            t = " at line " + str(line)
        return self.code + " " + self.name + t + "."

    def what_long(self, line: int, args: [str]) -> str:     
        """Function (lambda in fact) generating a verbose description of the error/warning.
        By default it returns the short description with an information that no verbose version was defined.
        Verbose definition can be defined in attirbute self.verbose as lambda args:

        Can throw IndexError

        Args:
            line (int):     line at which the error/warning was encountered.
            args ([str]):   list of additional arguments used to produce the verbose error description
                                e.g. macro name
        """
        return self.what_short(line) + " " + self.verbose(args)