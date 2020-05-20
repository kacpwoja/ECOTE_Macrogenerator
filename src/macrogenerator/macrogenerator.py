""" Main Macro Generator class
"""

from macro import Macro
from macrolibrary import MacroLibrary
from errorlibrary import get_error_lib
from log import Log

class MacroGenerator():
    def __init__(self):
        self.macro_library = MacroLibrary()

    def transform(self, source_text: str) -> (str, [Log]):
        """ TODO
        """
        output_text = source_text
        logs = []

        return output_text, logs

    def __macro_definition(self, source_text: str) -> None:
        """ TODO
        """
        pass

    def __macro_call(self, source_text: str) -> str:
        """ TODO
        """
        return ""