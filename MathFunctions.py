import math
import operator


class MathFunctions():
    @staticmethod
    def is_unary(x):
        """
        Return true if x is a unary operator. False otherwise.
        Parameters:
            x - Mathematical operator of type String.
        """
        if x in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'sqrt']:
            return True
        return False

    @staticmethod
    def is_binary(x):
        """
        Return true if x is a binary operator. False otherwise.
        Parameters:
            x - Mathematical operator of type String.
        """
        if x in ['+', '-', '*', '/', '^']:
            return True
        return False

    @staticmethod
    def get_unary(x):
        """
        Return the mathematical function equivalent of x.
        Parameters:
            x - Mathematical operator of type String.
        """
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

    @staticmethod
    def get_binary(x):
        """
        Return the mathematical function equivalent of x.
        Parameters:
            x - Mathematical operator of type String.
        """
        # Dictionary of possible binary operators in an expression.
        # Stores the character value, and the operator to perform for each character's operator.
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv,
                     '^': operator.pow}
        # Select the appropriate function for the current operator.
        return operators[x]