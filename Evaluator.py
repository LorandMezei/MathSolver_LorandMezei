import operator
import math

class Evaluator():
    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
    def evaluate(self, tree):
        # Get the left child of the tree.
        left_child = tree.getLeftChild()
        # Get the right child of the tree.
        right_child = tree.getRightChild()

        # Is an internal node (meaning root value is an operator).
        if left_child and right_child:
            # Select the appropriate operator for the current operator.
            op = get_binary(tree.getRootVal())
            # Apply the operator to both the left child's value and the right child's value.
            # Recur into left child and right child.
            return op(float(self.evaluate(left_child)), float(self.evaluate(right_child)))

        else:
            return tree.getRootVal()

    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
    # Evaluate tree with variables.
    def evaluate_vars(self, tree, vars):
        # Get the left child of the tree.
        left_child = tree.getLeftChild()
        # Get the right child of the tree.
        right_child = tree.getRightChild()

        # Is an internal node (meaning root value is an operator).
        if left_child and right_child:
            # If operator is a unary function.
            if is_unary(tree.getRootVal()):
                # Select the appropriate function for the current operator.
                fun = get_unary(tree.getRootVal())
                # Apply the operator to only the right child.
                # Recur into right child only.
                return fun(float(self.evaluate_vars(right_child, vars)))

            # Operator is binary.
            elif is_binary(tree.getRootVal()):
                # Select the appropriate operator for the current operator.
                op = get_binary(tree.getRootVal())
                # Apply the operator to both the left child's value and the right child's value.
                # Recur into left child and right child.
                return op(float(self.evaluate_vars(left_child, vars)), float(self.evaluate_vars(right_child, vars)))

        # Is a leaf node (meaning root value is not an operator).
        else:
            # If operand is a variable.
            if tree.getRootVal() in vars:
                return vars[tree.getRootVal()]

            # If operator is a digit.
            elif tree.getRootVal() not in vars:
                return tree.getRootVal()

def is_unary(x):
    if x in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'sqrt']:
        return True
    return False

def is_binary(x):
    if x in ['+', '-', '*', '/', '^']:
        return True
    return False

def get_unary(x):
    # Dictionary of possible unary functions in an expression.
    # Stores the character value, and the function to perform for each string's function.
    functions = {'sin': math.sin,
                 'cos': math.cos,
                 'tan': math.tan,
                 'arcsin': math.asin,
                 'arccos': math.acos,
                 'arctan': math.atan,
                 'sqrt': math.sqrt}
    # Select the appropriate function for the current operator.
    return functions[x]

def get_binary(x):
    # Dictionary of possible binary operators in an expression.
    # Stores the character value, and the operator to perform for each character's operator.
    operators = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.truediv,
                 '^': operator.pow}
    # Select the appropriate function for the current operator.
    return operators[x]


