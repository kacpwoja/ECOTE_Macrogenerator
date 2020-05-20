"""Module handling the library of all existing errors
"""

from error import Error
from log import Log

class ErrorLibException(Exception):
    """Exception for internat errors of the library
    """
    def __init__(self, message):
        """
        Args:
            message (str):  the internal error message
        """
        self.message = message

class ErrorLibrary():
    """Class for storing an error library

    Attributes:
        library [Error]:    the list of errors/warnings in the library
    """
    def __init__(self):
        self.library = []
    
    def get_error(self, code: str) -> Error:
        """Gets the error from the library given an error code

        Can throw ErrorLibException

        Args:
            code (str):     the code of the error
        """
        for er in self.library:
            if er.code == code:
                return er

        raise ErrorLibException("Error code not in library")

    def what_short(self, log: Log) -> str:
        """Gets the short description of an error given a Log

        Can throw ErrorLibException

        Args:
            log (Log):      log on basis of which to generate the error message
        """
        return self.get_error(log.err_code).what_short(log.line)

    def what_long(self, log: Log) -> str:
        """Gets the verbose description of an error given a Log

        Can throw ErrorLibException

        Args:
            log (Log):      log on basis of which to generate the error message
        """
        return self.get_error(log.err_code).what_long(log.line, log.args)

def get_error_lib():
    """Gets the error library with the defined errors.
    """
    lib = ErrorLibrary()

    #...

    return lib