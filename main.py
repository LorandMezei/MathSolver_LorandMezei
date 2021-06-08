import re
import numpy as np
import pandas as pd
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator
import math

class Tokenizer():
    def tokenize_math_eq(self, eq):
        tokens = np.array(eq.split('=')) #tokens[0] (left side of '=') and tokens[1] (right side of '=')
        tokens_left = np.array([tokens[0]])
        tokens_right = np.array(self.tokenize_math_exp(tokens[1]))
        return np.concatenate((tokens_left, ["="], tokens_right))

    #https://stackoverflow.com/questions/20805614/tokenize-a-mathematical-expression-in-python, by koffein
    def tokenize_math_exp(self, exp):
        return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\^\/])", exp)

#https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
class Evaluator():
    def evaluate(self, tree):
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv,
                     '^': operator.pow,}

        left_child = tree.getLeftChild()
        right_child = tree.getRightChild()

        if left_child and right_child:
            function = operators[tree.getRootVal()]
            return function(float(self.evaluate(left_child)), float(self.evaluate(right_child)))
        else:
            return tree.getRootVal()

#https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
class ExpTreeBuilder():
    def build_exp_tree(self, exp):
        parent_stack = Stack()
        exp_tree = BinaryTree('')
        parent_stack.push(exp_tree)
        current_tree = exp_tree

        for i in exp:
            if i == '(':
                current_tree.insertLeft('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getLeftChild()

            elif i in ['+', '-', '*', '/', '^']:
                current_tree.setRootVal(i)
                current_tree.insertRight('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getRightChild()

            elif i == ')':
                current_tree = parent_stack.pop()

            elif i not in ['+', '-', '*', '/', '^', ')']:
                current_tree.setRootVal(i)
                parent = parent_stack.pop()
                current_tree = parent

        return exp_tree

def main():
    tk = Tokenizer()
    exp = tk.tokenize_math_exp("((5^2)*(4-2))")

    etb = ExpTreeBuilder()
    tree = etb.build_exp_tree(exp)

    ev = Evaluator()
    value = ev.evaluate(tree)
    print(value)

if __name__ == "__main__":
    main()