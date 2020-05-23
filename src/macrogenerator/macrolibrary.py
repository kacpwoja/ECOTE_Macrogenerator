from .macro import Macro

class MacroLibException(Exception):
    """Exception for internat errors of the library
    """
    def __init__(self, message: str):
        """
        Args:
            message (str):  the internal error message
        """
        self.message = message

class MacroLibrary():
    """ Class for storing macros
    """
    def __init__(self):
        self.library = []

    def get_macro(self, name: str) -> Macro:
        """ Gets a macro from library given a macro name

        Can throw MacroLibException

        Args:
            name (str):         name of the macro to get
        """
        for m in self.library:
            if m.name == name:
                return m

        raise MacroLibException("Macro not found in library")

    def insert_macro(self, element: Macro) -> None:
        """ Adds a Macro to the library

        Can throw MacroLibException

        Args:
            element (Macro):    Macro to add
        """
        for m in self.library:
            if m.name == element.name:
                raise MacroLibException("Macro already defined")

        self.library.append(element)