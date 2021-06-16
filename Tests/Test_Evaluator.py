import unittest

class Test_Evaluator(unittest.TestCase):
    exp1 = ['(', '(', 'cos', '(', 'x', ')', ')', '*', '(', 'sin', '(', 'y', ')', ')', ')']
    exp2 = ['(', '(', '1', '+', '2', ')', '*', '(', '3', '+', '4', ')', ')']
    exp3 = ['(', 'cos', '(', '2', '*', 'x', ')', ')']
    exp4 = ['(', 'x', '+', '(', '(', 'x', '+', '5', ')', '^', '2', ')', ')']
    exp5 = ['(', '1', '*', '(', '2', '*', '3', ')', ')']
    exp6 = ['(', 'x', ')']
    exp7 = ['(', '-', 'x', ')']

    def test_evaluate(self):
        pass

    def test_evaluate_vars(self):
        pass

if __name__ == '__main__':
    unittest.main()