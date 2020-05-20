class Macro():
    """ Class describing a macro
    """
    def __init__(self, name: str, arguments: [str], body: str):
        """
        Args:
            name (str):         name of the macro
            arguments ([str]):  argument names in the macro
            body (str):         macro body
        """
        self.name = name
        self.arguments = arguments
        self.body = body