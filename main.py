import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator
import math

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

class Evaluator():
    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
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

        # If both left child and right child are not empty (meaning root value is an operator).
        if left_child and right_child:
            # Select the appropriate operator for the current operator.
            op = operators[tree.getRootVal()]
            # Apply the operator to both the left child's value and the right child's value.
            # Recur into left child and right child.
            return op(float(self.evaluate(left_child)), float(self.evaluate(right_child)))
        else:
            return tree.getRootVal()

    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
    # Evaluate tree with variables.
    def evaluate_vars(self, tree, vars):
        # Dictionary of possible binary operators in an expression.
        # Stores the character value, and the operator to perform for each character's operator.
        operators = {'+': operator.add,
                     '-': operator.sub,
                     '*': operator.mul,
                     '/': operator.truediv,
                     '^': operator.pow}
        # Dictionary of possible unary functions in an expression.
        # Stores the character value, and the function to perform for each string's function.
        functions = {'sin': math.sin,
                     'cos': math.cos,
                     'tan': math.tan,
                     'arcsin': math.asin,
                     'arccos': math.acos,
                     'arctan': math.atan,
                     'sqrt': math.sqrt}

        # Get the left child of the tree.
        left_child = tree.getLeftChild()
        # Get the right child of the tree.
        right_child = tree.getRightChild()

        # If both left child and right child are not empty (meaning root value is an operator).
        if left_child and right_child:
            # If operator is a unary function.
            if is_unary(tree.getRootVal()):
                # Select the appropriate function for the current operator.
                fun = functions[tree.getRootVal()]
                # Apply the operator to only the right child.
                # Recur into right child only.
                return fun(float(self.evaluate_vars(right_child, vars)))
            # Operator is binary.
            else:
                # Select the appropriate operator for the current operator.
                op = operators[tree.getRootVal()]
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

class Grapher():
    def x_1to10(self, tree, ev):
        vars = {'x': 1}
        x = np.array([])
        y = np.array([])
        for i in range(1, 11):
            value = ev.evaluate_vars(tree, vars)
            x = np.append(x, i)
            y = np.append(y, value)
            vars['x'] += 1
        return [x, y]

class ExpTreeBuilder():
    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
    # Build a binary expression tree from a !FULLY PARENTHESIZED! mathematical expression.
    def build_exp_tree(self, exp):
        parent_stack = Stack()  # Stack to hold the parent pointers.
        current_tree = BinaryTree('')  # Empty expression tree using a binary tree.
        parent_stack.push(current_tree)  # Push the empty expression tree into the parent stack.

        # For each character in the mathematical expression.
        # Parenthesis do not get stored in the expression tree.
        for i in exp:
            # If current character is a left parenthesis.
            if i == '(':
                # Create an empty left child.
                current_tree.insertLeft('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getLeftChild()
            # If current character is a binary operator.
            elif is_binary(i):
                current_tree.setRootVal(i)
                # Create an empty right child.
                current_tree.insertRight('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getRightChild()
            # If current string is a unary function.
            elif is_unary(i):
                current_tree.setRootVal(i)
                # Create an empty right child.
                current_tree.insertRight('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getRightChild()
            # If current character is a right parenthesis.
            elif i == ')':
                current_tree = parent_stack.pop()
            # If current character is not an operator and not a right parenthesis.
            # Digit or variable.
            elif not is_unary(i) and not is_binary(i) and i != ')':
                current_tree.setRootVal(i)
                # Take parent out of the stack.
                parent = parent_stack.pop()
                # Go back to the parent node.
                current_tree = parent
        # Return the completed expression tree.
        return current_tree

def is_unary(i):
    if i in ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'sqrt']:
        return True
    return False

def is_binary(i):
    if i in ['+', '-', '*', '/', '^']:
        return True
    return False

def main():
    # Expression examples.
    exp1 = "((cos(1))*(sin(1)) + (1-2))"
    exp2 = "((1+2)*(3+4))"
    exp3 = "(cos(x))"
    exp4 = "(x+((x+5)^2))"
    exp5 = "(1*(2*3))"
    exp6 = "(x)"
    exp7 = "((-x) + 1)"

    # Tokenize mathematical expression.
    tk = Tokenizer()
    exp = tk.tokenize_math_exp(exp2)  #<--------------------------------------------------------------------------------

    # Build the expression tree from the tokenized mathematical expression.
    etb = ExpTreeBuilder()
    tree = etb.build_exp_tree(exp)

    # Traverse and print the expression tree in order.
    #pr = Printer()
    #pr.inorder(tree)
    #pr.print2D(tree)

    # Traverse and evaluate the expression tree in order.
    #ev = Evaluator()
    #value = ev.evaluate_vars(tree, {'x': 1})
    #print(value)
    #gr = Grapher()
    #graph_values = gr.x_1to10(tree, ev)
    #plt.plot(graph_values[0], graph_values[1])
    #plt.show()

if __name__ == "__main__":
    main()