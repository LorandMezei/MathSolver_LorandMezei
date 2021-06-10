import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

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
            return op(float(self.evaluate_vars(left_child, vars)), float(self.evaluate_vars(right_child, vars)))
        else:
            # If operand is a variable.
            if tree.getRootVal() in vars:
                return vars[tree.getRootVal()]
            # If operator is a digit.
            elif tree.getRootVal() not in vars:
                return tree.getRootVal()

class Printer():
    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
    def inorder(self, tree):
        if tree != None:
            self.inorder(tree.getLeftChild())
            print("'" + tree.getRootVal() + "'")
            self.inorder(tree.getRightChild())

    # https: // www.geeksforgeeks.org / print - binary - tree - 2 - dimensions /
    # Function to print binary tree in 2D
    # It does reverse inorder traversal
    def print2DUtil(self, root, space):
        # Base case
        if root == None:
            return

        # Increase distance between levels
        space += self.COUNT[0]

        # Process right child first
        self.print2DUtil(root.getRightChild(), space)

        # Print current node after space
        # count
        print()
        for i in range(self.COUNT[0], space):
            print(end=" ")
        print(root.getRootVal())

        # Process left child
        self.print2DUtil(root.getLeftChild(), space)

    # https: // www.geeksforgeeks.org / print - binary - tree - 2 - dimensions /
    # Wrapper over print2DUtil()
    COUNT = [10]
    def print2D(self, root):
        # space=[0]
        # Pass initial space count as 0
        self.print2DUtil(root, 0)

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
        exp_tree = BinaryTree('')  # Empty expression tree using a binary tree.
        parent_stack.push(exp_tree)  # Push the empty expression tree into the parent stack.
        current_tree = exp_tree  # Current tree is assigned to the empty expression tree.

        # For each character in the mathematical expression.
        for i in exp:
            # If current character is a left parenthesis.
            if i == '(':
                current_tree.insertLeft('')
                parent_stack.push(current_tree)
                current_tree = current_tree.getLeftChild()
            # If current character is an operator.
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
    # Expression examples.
    exp1 = "((cos(x))*(sin(x)))"
    exp2 = "((1+2)*(3+4))"
    exp3 = "(cos(1))"
    exp4 = "(x+((x+5)^2))"
    exp5 = "(1*(2*3))"
    exp6 = "(x)"
    exp7 = "(x^2)"

    # Tokenize mathematical expression.
    tk = Tokenizer()
    exp = tk.tokenize_math_exp(exp7)  #<--------------------------------------------------------------------------------
    print(exp)

    # Build the expression tree from the tokenized mathematical expression.
    etb = ExpTreeBuilder()
    tree = etb.build_exp_tree(exp)

    # Traverse and print the expression tree in order.
    pr = Printer()
    pr.inorder(tree)
    pr.print2D(tree)

    # Traverse and evaluate the expression tree in order.
    ev = Evaluator()
    gr = Grapher()
    graph_values = gr.x_1to10(tree, ev)
    plt.plot(graph_values[0], graph_values[1])
    plt.show()

if __name__ == "__main__":
    main()