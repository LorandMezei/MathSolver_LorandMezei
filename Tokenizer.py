import re


class Tokenizer():
    # https://stackoverflow.com/questions/20805614/tokenize-a-mathematical-expression-in-python, by koffein
    def tokenize_math_exp(self, exp):
        # Tokenize the mathematical expression using a regular expression.
        # Should split expression by operands, operators, and functions.
        return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\^\/])", exp)