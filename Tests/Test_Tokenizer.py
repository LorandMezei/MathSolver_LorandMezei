import unittest
from Tokenizer import Tokenizer

class Test_Tokenizer(unittest.TestCase):
    # Expression examples.
    exp1 = "((cos(x)) * (sin(y)))"
    exp2 = "((1+2)*(3+4))"
    exp3 = "(cos(2*x))"
    exp4 = "(x+((x+5)^2))"
    exp5 = "(1*(2*3))"
    exp6 = "(x)"
    exp7 = "(-x)"

    tk = Tokenizer()

    def test_tokenize_math_exp(self):
        self.assertEqual(self.tk.tokenize_math_exp(self.exp1),
                         ['(', '(', 'cos', '(', 'x', ')', ')', '*', '(', 'sin', '(', 'y', ')', ')', ')'])
        self.assertEqual(self.tk.tokenize_math_exp(self.exp2),
                         ['(', '(', '1', '+', '2', ')', '*', '(', '3', '+', '4', ')', ')'])
        self.assertEqual(self.tk.tokenize_math_exp(self.exp3),
                         ['(', 'cos', '(', '2', '*', 'x', ')', ')'])
        self.assertEqual(self.tk.tokenize_math_exp(self.exp4),
                         ['(', 'x', '+', '(', '(', 'x', '+', '5', ')', '^', '2', ')', ')'])
        self.assertEqual(self.tk.tokenize_math_exp(self.exp5),
                         ['(', '1', '*', '(', '2', '*', '3', ')', ')'])
        self.assertEqual(self.tk.tokenize_math_exp(self.exp6),
                         ['(', 'x', ')'])
        self.assertEqual(self.tk.tokenize_math_exp(self.exp7),
                         ['(', '-', 'x', ')'])

if __name__ == '__main__':
    unittest.main()