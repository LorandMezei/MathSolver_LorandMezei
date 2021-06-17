from pythonds.basic import Stack
from pythonds.trees import BinaryTree
from MathFunctions import MathFunctions

class ExpTreeBuilder():
    # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html
    # Build a binary expression tree from a TOKENIZED FULLY PARENTHESIZED mathematical expression.
    def build_exp_tree(self, exp):
        parent_stack = Stack()  # Stack to hold the pointers to the current tree's parents.
        current_tree = BinaryTree('')  # Empty string expression tree using a binary tree that will start as the current tree.
        parent_stack.push(current_tree)  # Push the empty expression tree into the parent stack.

        # For each character in the mathematical expression.
        # Parenthesis do not get stored in the expression tree.
        for i in exp:
            # If current character is a left parenthesis.
            if i == '(':
                # Create an empty tree and assign it to current tree's left child.
                current_tree.insertLeft('')
                # Push the current tree pointer into the parent stack.
                parent_stack.push(current_tree)
                # Move the pointer of the current tree to point to the current tree's left child.
                current_tree = current_tree.getLeftChild()

            # If current character is a binary operator.
            elif MathFunctions.is_binary(i):
                # Set the current tree's value to i.
                current_tree.setRootVal(i)
                # Create an empty tree and assign it to current tree's right child.
                current_tree.insertRight('')
                # Push the current tree pointer into the parent stack.
                parent_stack.push(current_tree)
                # Move the pointer of the current tree to point to the current tree's right child.
                current_tree = current_tree.getRightChild()

            # If current string is a unary function.
            elif MathFunctions.is_unary(i):
                # Set the current tree's value to i.
                current_tree.setRootVal(i)
                # Create an empty tree and assign it to current tree's right child.
                current_tree.insertRight('')
                # Push the current tree pointer into the parent stack.
                parent_stack.push(current_tree)
                # Move the pointer of the current tree to point to the current tree's right child.
                current_tree = current_tree.getRightChild()

            # If current character is a right parenthesis.
            elif i == ')':
                # Move the pointer of the current tree to point to the top tree in the parent stack.
                current_tree = parent_stack.pop()

            # If current character is not an operator and not a right parenthesis.
            # is a digit or variable.
            elif not MathFunctions.is_unary(i) and not MathFunctions.is_binary(i) and i != ')':
                # Set the current tree's value to i.
                current_tree.setRootVal(i)
                # Take top parent tree out of the stack and move the current tree pointer to point back to that parent.
                current_tree = parent_stack.pop()

        # Return the completed expression tree.
        return current_tree