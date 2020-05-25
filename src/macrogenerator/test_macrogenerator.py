import unittest

from .macrogenerator import MacroGenerator
from error.log import Log

class TestMacroGenerator(unittest.TestCase):
    """ Tests for the MacroGenerator class
    """
    def __init__(self, *args, **kwargs):
        super(TestMacroGenerator, self).__init__(*args, **kwargs)
        self.generator = MacroGenerator()

    # Correct Usage
    def test_c_simple_macro(self):
        text_in = \
            """#MACRO(){test macro}
            $MACRO()"""
        text_out = \
            """test macro"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))

    def test_c_macro_w_args(self):
        text_in = \
            """#MACRO(P1, P2)
            {&P1&+&P2&*&P1&}
            $MACRO(34,20)"""
        text_out = \
            """34+20*34"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))
        
    def test_c_multiple_macros(self):
        text_in = \
            """#MACRO1(){test macro}
            #MACRO2(P1, P2)
            {&P1&+&P2&*&P1&}
            $MACRO2(34,20)
            $MACRO1()"""
        text_out = \
            """34+20*34
            test macro"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))
        
    def test_c_multiple_macros_and_free(self):
        text_in = \
            """free text
            #MACRO1(){test macro}
            #MACRO2(P1, P2)
            {&P1&+&P2&*&P1&}
            $MACRO2(34,20)
            $MACRO1()
            MORE TEXT"""
        text_out = \
            """free text
            34+20*34
            test macro
            MORE TEXT"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))
        
    def test_c_escape_in_text(self):
        text_in = \
            """Price: \\$20"""
        text_out = \
            """Price: $20"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))
        
    def test_c_escape_in_body(self):
        text_in = \
            """#MACRO(A){B\\&&A&}
            $MACRO(C)"""
        text_out = \
            """B&C"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))
        
    def test_c_escape_in_arg(self):
        text_in = \
            """#MACRO(A){hello &A&}
            $MACRO(big \\$)"""
        text_out = \
            """hello big $"""
        self.assertEqual(self.generator.transform(text_in), (text_out, []))

    # Macro Definition Errors
    def test_e10(self):
        text_in = \
            """#MY MACRO(){test macro}"""
        err = "e10"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e11(self):
        text_in = \
            """#MACRO(P1, P2){&P1&+&P2&}
            #MACRO(){hello}"""
        err = "e11"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e12(self):
        text_in = \
            """#MACRO(MY PARAM)
            {&MY PARAM& is wrong}"""
        err = "e12"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e13(self):
        text_in = \
            """#MACRO()eee{test macro}"""
        err = "e13"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e14(self):
        text_in = \
            """#MACRO(P1, P2)
            {&P1& is less than &P3&}"""
        err = "e14"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e15(self):
        text_in = \
            """#HI(){hello}
            #MACRO(ARG){$HI &ARG&}"""
        err = "e15"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e16(self):
        text_in = \
            """#MACRO(){#NEST(){no}$NEST}"""
        err = "e16"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e17(self):
        text_in = \
            """#MACRO(A,A){}"""
        err = "e17"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e18(self):
        text_in = \
            """#MACRO("""
        err = "e18"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)

    # Macro Call Errors
    def test_e20(self):
        text_in = \
            """$MACRO(hello)"""
        err = "e20"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e21(self):
        text_in = \
            """#MACRO(P1, P2){&P1&+&P2&}
            $MACRO(23)"""
        err = "e21"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e22(self):
        text_in = \
            """#MYMACRO(P){&P& is good}
            $MY MACRO(John)"""
        err = "e22"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e23(self):
        text_in = \
            """#A(P){hello &P&}
            #B(){John}
            $A($B)"""
        err = "e23"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e24(self):
        text_in = \
            """#A(P){hello &P&}
            $A(#B(){John})"""
        err = "e24"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)
        
    def test_e25(self):
        text_in = \
            """#A(P){hello &P&}
            $A("""
        err = "e25"
        with self.assertRaises(Log) as cm:
            self.generator.transform(text_in)
        self.assertEqual(cm.exception.err_code, err)

    # Macro Definition Warnings
    def test_w10(self):
        text_in = \
            """#MACRO(P){test macro}
            $MACRO(11)"""
        text_out = \
            """test macro"""
        warn = "w10"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)
        
    def test_w11(self):
        text_in = \
            """#MACRO(){}
            $MACRO()"""
        text_out = \
            """"""
        warn = "w11"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)
        
    def test_w12(self):
        text_in = \
            """#MACRO(P){test macro &P&}"""
        text_out = \
            """"""
        warn = "w12"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)

    # Macro Call Warnings
    def test_w20(self):
        text_in = \
            """#MACRO(){test macro}
            $MACRO(John)"""
        text_out = \
            """test macro"""
        warn = "w20"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)
        
    def test_w21(self):
        text_in = \
            """#MACRO(P1, P2){&P1&+&P2&}
            $MACRO(,34)"""
        text_out = \
            """+34"""
        warn = "w21"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)
        
    def test_w22(self):
        text_in = \
            """#MACRO(P1, P2){&P1&+&P2&}
            $MACRO(34, 2)"""
        text_out = \
            """34+ 2"""
        warn = "w22"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)

    # Other Warnings
    def test_w90(self):
        text_in = \
            """\\a"""
        text_out = \
            """a"""
        warn = "w90"
        (out_str, out_log) = self.generator.transform(text_in)
        self.assertEqual(out_str, text_out)
        self.assertEqual(len(out_log), 1)
        self.assertEqual(out_log[0].err_code, warn)