import re
import numpy as np

class Tokenizer():
    def tokenize_math_eq(self, eq):
        # Split the mathematical equation into two parts: left of equals sign, right of equals sign.
        tokens = np.array(eq.split('='))  #tokens[0] (left side) and tokens[1] (right side)
        # Create an array that holds the tokens of the left side.
        tokens_left = np.array([tokens[0]])
        # Create an array that holds the tokens of the right side. This will further tokenize the right side expression.
        tokens_right = np.array(self.tokenize_math_exp(tokens[1]))
        # Concatenate left and right back together into a full equation.
        return np.concatenate((tokens_left, ["="], tokens_right))

    #https://stackoverflow.com/questions/20805614/tokenize-a-mathematical-expression-in-python, by koffein
    def tokenize_math_exp(self, exp):
        # Tokenize the mathematical expression using a regular expression.
        # Should split expression by operands, operators, and functions.
        return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\^\/])", exp)