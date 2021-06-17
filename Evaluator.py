from MathFunctions import MathFunctions


class Evaluator():
    @staticmethod
    def evaluate(tree):
        """
        Return the value of the tree.
        Parameters:
            tree - Binary expression tree that does not contain variables.
        """
        # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html

        # Get the left child of the tree.
        left_child = tree.getLeftChild()
        # Get the right child of the tree.
        right_child = tree.getRightChild()

        # Is an internal node (meaning root value is an operator).
        if left_child and right_child:
            # Select the appropriate operator for the current operator.
            op = MathFunctions.get_binary(tree.getRootVal())
            # Apply the operator to both the left child's value and the right child's value.
            # Recur into left child and right child.
            return op(float(Evaluator.evaluate(left_child)), float(Evaluator.evaluate(right_child)))

        else:
            return tree.getRootVal()

    @staticmethod
    def evaluate_vars(tree, vars):
        """
        Return the value of the tree.
        Parameters:
            tree - Binary expression tree that contains variables.
        """
        # https://runestone.academy/runestone/books/published/pythonds/Trees/ParseTree.html

        # Get the left child of the tree.
        left_child = tree.getLeftChild()
        # Get the right child of the tree.
        right_child = tree.getRightChild()

        # Is an internal node (meaning root value is an operator).
        if left_child and right_child:
            # If operator is a unary function.
            if MathFunctions.is_unary(tree.getRootVal()):
                # Select the appropriate function for the current operator.
                fun = MathFunctions.get_unary(tree.getRootVal())
                # Apply the operator to only the right child.
                # Recur into right child only.
                return fun(float(Evaluator.evaluate_vars(right_child, vars)))

            # Operator is binary.
            elif MathFunctions.is_binary(tree.getRootVal()):
                # Select the appropriate operator for the current operator.
                op = MathFunctions.get_binary(tree.getRootVal())
                # Apply the operator to both the left child's value and the right child's value.
                # Recur into left child and right child.
                return op(float(Evaluator.evaluate_vars(left_child, vars)), float(Evaluator.evaluate_vars(right_child, vars)))

        # Is a leaf node (meaning root value is not an operator).
        else:
            # If operand is a variable.
            if tree.getRootVal() in vars:
                return vars[tree.getRootVal()]

            # If operator is a digit.
            elif tree.getRootVal() not in vars:
                return tree.getRootVal()
