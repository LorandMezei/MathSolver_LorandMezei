import re
import numpy as np
import pandas as pd
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator
import math

class Tokenizer():
    def tokenize_math_eq(self, eq):
        # Split the mathematical expression into two parts: left of equals sign, right of equals sign.
        tokens = np.array(eq.split('=')) #tokens[0] (left side of '=') and tokens[1] (right side of '=')
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

#https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
class Evaluator():
    def evaluate(self, tree):
        # Dictionary of possible binary operators in an expression.
        # Stores the character value, and the operator to perform for each character's operator.
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv,
                     '^': operator.pow,}

        # Get the left child of the tree.
        left_child = tree.getLeftChild()
        # Get the right child of the tree.
        right_child = tree.getRightChild()

        # If both left child and right child are not empty (meaning root value is an operator)
        if left_child and right_child:
            # Select the appropriate operator for the current operator.
            function = operators[tree.getRootVal()]
            # Apply the operator to both the left child's value and the right child's value.
            # Recur into left child and right child.
            return function(float(self.evaluate(left_child)), float(self.evaluate(right_child)))
        else:
            # Else the root value is not an operator.
            return tree.getRootVal()

#https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
class Printer():
    def inorder(self, tree):
        if tree != None:
            self.inorder(tree.getLeftChild())
            print(tree.getRootVal())
            self.inorder(tree.getRightChild())

#https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
class ExpTreeBuilder():
    def build_exp_tree(self, exp):
        parent_stack = Stack() # Stack to hold the parent pointers.
        exp_tree = BinaryTree('') # Empty expression tree using a binary tree.
        parent_stack.push(exp_tree) # Push the empty expression tree into the parent stack.
        current_tree = exp_tree # Current tree is assigned to the empty expression tree.

        # For each character in the mathematical expression.
        for i in exp:
            # If current character is a left parenthesis
            if i == '(':
                current_tree.insertLeft('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getLeftChild()
            # If current character is an operator
            elif i in ['+', '-', '*', '/', '^']:
                current_tree.setRootVal(i)
                current_tree.insertRight('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getRightChild()
            # If current character is a right parenthesis.
            elif i == ')':
                current_tree = parent_stack.pop()
            # If current character is not an operator and not a right parenthesis.
            elif i not in ['+', '-', '*', '/', '^', ')']:
                current_tree.setRootVal(i)
                parent = parent_stack.pop()
                current_tree = parent
        # Return the completed expression tree.
        return exp_tree

def main():
    # Tokenize mathematical expression.
    tk = Tokenizer()
    exp = tk.tokenize_math_exp("(2*sin(x)+1)")

    # Build the expression tree from the tokenized mathematical expression.
    etb = ExpTreeBuilder()
    tree = etb.build_exp_tree(exp)

    # Traverse the expression tree in order.
    pr = Printer()
    pr.inorder(tree)

    # Evaluate the expression tree.
    ev = Evaluator()
    value = ev.evaluate(tree)

if __name__ == "__main__":
    main()