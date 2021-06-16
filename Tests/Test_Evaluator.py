import unittest

class Test_Evaluator(unittest.TestCase):
    exp1 = ['(', '(', 'cos', '(', 'x', ')', ')', '*', '(', 'sin', '(', 'y', ')', ')', ')']
    exp2 = ['(', '(', '1', '+', '2', ')', '*', '(', '3', '+', '4', ')', ')']
    exp3 = ['(', 'cos', '(', '2', '*', 'x', ')', ')']
    exp4 = ['(', 'x', '+', '(', '(', 'x', '+', '5', ')', '^', '2', ')', ')']
    exp5 = ['(', '1', '*', '(', '2', '*', '3', ')', ')']
    exp6 = ['(', 'x', ')']
    exp7 = ['(', '-', 'x', ')']

    etb = ExpTreeBuilder()
    ev = Evaluator()

#-------------------------------------------------------------------------------------------------------------------
    def test_evaluate_vars_exp1(self):
        tree = etb.build_exp_tree(self.exp1)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), 0.45464871341) # Radians.

    def test_evaluate_vars_exp2(self):
        tree = etb.build_exp_tree(self.exp2)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), 21)

    def test_evaluate_vars_exp3(self):
        tree = etb.build_exp_tree(self.exp3)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), -0.41614683654) # Radians.

    def test_evaluate_vars_exp4(self):
        tree = etb.build_exp_tree(self.exp4)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), 37)

    def test_evaluate_vars_exp5(self):
        tree = etb.build_exp_tree(self.exp5)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), 6)

    def test_evaluate_vars_exp6(self):
        tree = etb.build_exp_tree(self.exp6)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), 1)

    def test_evaluate_vars_exp7(self):
        tree = etb.build_exp_tree(self.exp7)
        self.assertEqual(self.ev.evaluate_vars(tree, {'x': 1}), -1)
#-------------------------------------------------------------------------------------------------------------------


    def test_evaluate_exp1(self):
        tree = etb.build_exp_tree(self.exp1)
    def test_evaluate_exp2(self):
        tree = etb.build_exp_tree(self.exp2)
    def test_evaluate_exp3(self):
        tree = etb.build_exp_tree(self.exp3)
    def test_evaluate_exp4(self):
        tree = etb.build_exp_tree(self.exp4)
    def test_evaluate_exp5(self):
        tree = etb.build_exp_tree(self.exp5)
    def test_evaluate_exp6(self):
        tree = etb.build_exp_tree(self.exp6)
    def test_evaluate_exp7(self):
        tree = etb.build_exp_tree(self.exp7)

if __name__ == '__main__':
    unittest.main()