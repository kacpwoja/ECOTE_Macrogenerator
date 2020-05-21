""" Main Macro Generator class
"""

from macrogenerator.macro import Macro
from macrogenerator.macrolibrary import MacroLibrary, MacroLibException
from error.errorlibrary import get_error_lib
from error.log import Log
from symbol.symbol import *

class MacroGenerator():
    def __init__(self):
        self.macro_library = MacroLibrary()
        self.line = 1

    def transform(self, source_text: str) -> (str, [Log]):
        """ TODO
        """
        output_text = ""
        logs = []
        self.line = 1

        while len(source_text) != 0:
            # get char
            char = source_text[0]
            source_text = source_text[1:]

            # switch
            if char == ESCAPE_CHARACTER:
                char = source_text[0]
                source_text = source_text[1:]
                output_text = output_text + char
                if not IS_SPECIAL(char):
                    logs.append(Log("w90", self.line, char))
                continue
            if char == SYMBOL_DEFINITION:
                try:
                    source_text = self.__macro_definition(source_text)
                except Log as err:
                    raise err
                continue
            if char == SYMBOL_CALL:
                (source_text, macro) = self.__macro_call(source_text)
                output_text = output_text + macro
                continue
            if char == "\n":
                self.line = self.line + 1

            output_text = output_text + char

        return output_text, logs

    def __macro_definition(self, source_text: str) -> str:
        """ TODO
        """
        name = ""
        args = []
        arg = ""
        body = ""

        # Extract name
        name_correct = True
        while len(source_text) != 0:
            char = source_text[0]
            source_text = source_text[1:]
            if char == SYMBOL_ARG_START:
                if name == "":
                    name_correct = False
                break
            if IS_SPECIAL(char) or char.isspace():
                name_correct = False
            name = name + char
        if not name_correct:
            raise Log("e10", self.line, [name])

        # Extract argument names
        arg_correct = True
        while len(source_text) != 0:
            char = source_text[0]
            source_text = source_text[1:]
            if char == SYMBOL_ARG_END:
                if not arg_correct:
                    raise Log("e12", self.line, [name, arg])
                if args.count(arg) != 0:
                    raise Log("e17", self.line, [name, arg])
                if arg != "":
                    args.append(arg)
                break
            if char == SYMBOL_ARG_SEPARATOR:
                if not arg_correct or arg == "":
                    raise Log("e12", self.line, [name, arg])
                if args.count(arg) != 0:
                    raise Log("e17", self.line, [name, arg])
                args.append(arg)
                arg = ""
                arg_correct = True
                continue
            if IS_SPECIAL(char):
                arg_correct = False
            if char.isspace() and arg != "":
                arg_correct = False
            if char == "\n":
                self.line = self.line + 1
            if char.isspace() and arg == "":
                continue
            arg = arg + char

        # Get body start
        while len(source_text) != 0:
            char = source_text[0]
            source_text = source_text[1:]
            if char == "\n":
                self.line = self.line + 1
            if char.isspace():
                continue
            if char == SYMBOL_BODY_START:
                break
            raise Log("e13", self.line, [name])
            
        # Extract body
        while len(source_text) != 0:
            char = source_text[0]
            source_text = source_text[1:]
            if char == ESCAPE_CHARACTER:
                char = source_text[0]
                source_text = source_text[1:]
                body = body + char
                continue
            if char == SYMBOL_BODY_END:
                while len(source_text) != 0:
                    char = source_text[0]
                    if not char.isspace():
                        break
                    if char == "\n":
                        self.line = self.line + 1
                    source_text = source_text[1:]
                break
            if char == SYMBOL_DEFINITION:
                raise Log("e16", self.line, [name])
            if char == SYMBOL_CALL:
                raise Log("e15", self.line, [name])
            if char == "\n":
                self.line = self.line + 1
            body = body + char
            if char == SYMBOL_ARGUMENT:
                arg = ""
                while len(source_text) != 0:
                    char = source_text[0]
                    source_text = source_text[1:]
                    if char == SYMBOL_ARGUMENT:
                        body = body + char
                        break
                    arg = arg + char
                    body = body + char
                if args.count(arg) == 0:
                    raise Log("e14", self.line, [name, arg])

        # Add to library
        try:
            self.macro_library.insert_macro(Macro(name, args, body))
        except MacroLibException:
            raise Log("e11", self.line, [name])

        return source_text

    def __macro_call(self, source_text: str) -> (str, str):
        """ TODO
        """
        return source_text, ""