import unittest
from .macrolibrary import MacroLibrary, MacroLibException
from .macro import Macro

class TestMacroLibrary(unittest.TestCase):
    """ Tests for the MacroLibrary class
    """
    def __init__(self, *args, **kwargs):
        super(TestMacroLibrary, self).__init__(*args, **kwargs)
        self.library = MacroLibrary()
        self.name = "MacroName"
        self.args = ["A", "B"]
        self.body = "body&A&body&B&"

    def test_init(self):
        self.assertEqual(len(self.library.library), 0)
        self.assertIsInstance(self.library.library, list)
        self.assertEqual(self.library.library, [])

    def test_insert(self):
        self.library.insert_macro(Macro(self.name, self.args, self.body))
        self.assertEqual(len(self.library.library), 1)
        self.assertEqual(self.library.library[0].name, self.name)
        self.assertEqual(self.library.library[0].arguments, self.args)
        self.assertEqual(self.library.library[0].body, self.body)

        with self.assertRaises(MacroLibException):
            self.library.insert_macro(Macro(self.name, self.args, self.body))
        self.assertEqual(len(self.library.library), 1)

    def test_get(self):
        with self.assertRaises(MacroLibException):
            self.library.get_macro("wrong name")

        self.library.insert_macro(Macro(self.name, self.args, self.body))
        macro = self.library.get_macro(self.name)
        self.assertEqual(macro.name, self.name)
        self.assertEqual(macro.arguments, self.args)
        self.assertEqual(macro.body, self.body)
        
        