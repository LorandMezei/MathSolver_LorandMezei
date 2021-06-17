import re


class Tokenizer():
    def tokenize_math_exp(self, exp):
        """
        Return an array of strings that contains the tokens of the mathematical expression.
        Parameters:
            exp - A string containing a fully-parenthesized mathematical expression.
        """
        # https://stackoverflow.com/questions/20805614/tokenize-a-mathematical-expression-in-python, by koffein
        # Tokenize the mathematical expression using a regular expression.
        # Should split expression by operands, operators, and functions.
        return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\^\/])", exp)