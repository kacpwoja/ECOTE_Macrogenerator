"""Module symbol.symbol

This module stores the special symbols used by the macrogenerator

They should be treated as constants and NOT be changed at runtime
"""

SYMBOL_DEFINITION = '#'
SYMBOL_CALL = '$'
SYMBOL_ARG_START = '('
SYMBOL_ARG_END = ')'
SYMBOL_BODY_START = '{'
SYMBOL_BODY_END = '}'
SYMBOL_ARGUMENT = '&'
SYMBOL_ARG_SEPARATOR = ','
ESCAPE_CHARACTER = '\\'

def IS_SPECIAL(char: str):
    return char == SYMBOL_DEFINITION or char == SYMBOL_CALL or char == SYMBOL_BODY_START or char == SYMBOL_BODY_END \
        or char == SYMBOL_ARGUMENT or char == SYMBOL_ARG_START or char == SYMBOL_ARG_END or char == SYMBOL_ARG_SEPARATOR \
            or char == ESCAPE_CHARACTER