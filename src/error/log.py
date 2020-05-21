class Log(Exception):
    """Class for storing the Logs of errors/warnings
    """
    def __init__(self, err_code: str, line: int, args: [str]):
        """
        Args:
            err_code (str):     code of the error/warning encountered
            line (int):         line at which the error/warning was encountered
            args ([str]):       list of additional arguments used to produce the verbose error description
                                    e.g. macro name
        """
        self.err_code = err_code
        self.line = line
        self.args = args