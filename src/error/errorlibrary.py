"""Module handling the library of all existing errors
"""

from .error import Error
from .log import Log

class ErrorLibException(Exception):
    """Exception for internat errors of the library
    """
    def __init__(self, message: str):
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

    # Errors

    # Macro Definition Errors
    # e10 args: 0 - name of incorrect macro
    e = Error("e10", "Incorrect Macro Name")
    e.verbose = lambda args: "Unexpected character encountered in macro \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e11 args: 0 - name of defined macro
    e = Error("e11", "Macro Already Defined")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" already defined."
    lib.library.append(e)
    
    # e12 args: 0 - name of the macro
    #           1 - name of incorrect parameter
    e = Error("e12", "Incorrect Parameter Name")
    e.verbose = lambda args: "Unexpected character encountered in parameter name \"" + args[1] + "\" in macro \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e13 args: 0 - name of macro missing a body
    e = Error("e13", "Missing Macro Body")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" is missing a body."
    lib.library.append(e)
    
    # e14 args: 0 - name of the macro
    #           1 - name of undefined parameter
    e = Error("e14", "Parameter Undefined")
    e.verbose = lambda args: "Parameter \"" + args[1] + "\" is not defined in macro \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e15 args: 0 - name of macro with call
    e = Error("e15", "Nested Call")
    e.verbose = lambda args: "Another macro called inside macro body of \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e16 args: 0 - name of macro with definition
    e = Error("e16", "Nested Definition")
    e.verbose = lambda args: "Another macro defined inside macro body of \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e17 args: 0 - name of the macro
    #           1 - name of repeated parameter
    e = Error("e17", "Parameter Repeated")
    e.verbose = lambda args: "Parameter \"" + args[1] + "\" is defined more than once in macro \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e18 args: 0 - name of macro with definition
    e = Error("e18", "Unfinished Definition")
    e.verbose = lambda args: "The input ended inside the definition of macro \"" + args[0] + "\"."
    lib.library.append(e)
    
    # Macro Call Errors
    # e20 args: 0 - name of undefined macro
    e = Error("e20", "Undefined Macro")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" was not defined."
    lib.library.append(e)
    
    # e21 args: 0 - name of macro in question
    #           1 - amount of used parameters
    #           2 - amount of needed parameters
    e = Error("e21", "Too Few Arguments")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" was called with " + args[1] + " parameters, but defined with " + args[2] + "."
    lib.library.append(e)
    
    # e22 args: 0 - name of incorrect macro
    e = Error("e22", "Incorrect Macro Call")
    e.verbose = lambda args: "Unexpected character encountered in macro call \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e23 args: 0 - name of macro with call
    e = Error("e23", "Nested Call")
    e.verbose = lambda args: "Another acro called inside macro call of \"" + args[0] + "\"."
    lib.library.append(e)
    
    # e24 args: 0 - name of macro with definition
    e = Error("e24", "Nested Definition")
    e.verbose = lambda args: "Another macro defined inside macro call of \"" + args[0] + "\"."
    lib.library.append(e)

    # e25 args: 0 - name of macro with definition
    e = Error("e25", "Unfinished Call")
    e.verbose = lambda args: "The input ended inside the call of macro \"" + args[0] + "\"."
    lib.library.append(e)

    # Other Errors
    # e98 args: 0 - message
    e = Error("e98", "I/O Error")
    e.verbose = lambda args: "There was an error with file I/O: " + args[0] + "."
    lib.library.append(e)

    # Warnings

    # Macro Definition Warnings
    # w10 args: 0 - name of the macro
    #           1 - name of the parameter
    e = Error("w10", "Unused Parameter")
    e.verbose = lambda args: "Parameter \"" + args[1] + "\" unused in macro \"" + args[0] + "\"."
    lib.library.append(e)
    
    # w11 args: 0 - name of macro with empty body
    e = Error("w11", "Empty Macro Body")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" has an empty body."
    lib.library.append(e)
    
    # w12 args: 0 - name of unused macro
    e = Error("w12", "Unused Macro")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" was defined, but not called."
    lib.library.append(e)

    # Macro Call Warnings
    
    # w20 args: 0 - name of the macro
    #           1 - amount of used parameters
    #           2 - amount of needed parameters
    e = Error("w20", "Too Many Arguments")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" was called with " + args[1] + " arguments, but defined with " + args[2] + "."
    lib.library.append(e)
    
    # w21 args: 0 - name of the macro
    #           1 - name of the argument
    e = Error("w21", "Empty Argument")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" was called with an empty argument \"" + args[1] + "\"."
    lib.library.append(e)

    # w22 args: 0 - name of the macro
    #           1 - name of the argument
    e = Error("w22", "Whitespace Argument")
    e.verbose = lambda args: "Macro \"" + args[0] + "\" was called with an argument \"" + args[1] + "\" starting with whitespace. Possibly unmeant behaviour."
    lib.library.append(e)

    # CLI Warnings
    # w80 args: 0 - filename
    e = Error("w80", "Overwrite Warning")
    e.verbose = lambda args: "The input file is the same as the output file: \"" + args[0] + "\"."
    lib.library.append(e)

    # Other Warnings
    # w90 args 0 - character
    e = Error("w90", "Escape Character Error")
    e.verbose = lambda args: "Escape Character was used on a non-special character: \'" + args[0] + "\'."
    lib.library.append(e)

    return lib

if __name__ == "__main__":
    # Printing macro library for debug purposes
    for e in get_error_lib().library:
        print(e.code + " " + e.name)
        print(e.what_short(10))
        print(e.what_long(20, ["arg0", "arg1", "arg2"]))