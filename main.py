from matplotlib import pyplot as plt
from Tokenizer import Tokenizer
from ExpTreeBuilder import ExpTreeBuilder
from Evaluator import Evaluator
from Grapher import Grapher


def main():
    # Expression examples.
    exp1 = "((cos(2*x)) * (sin(3/y)))"
    exp2 = "((1+2)*(3+4))"
    exp3 = "(cos(2*x))"
    exp4 = "(x+((x+5)^2))"
    exp5 = "(1*(2*3))"
    exp6 = "(x)"
    exp7 = "(-x)"

    # Tokenize mathematical expression.
    exp = Tokenizer.tokenize_math_exp(exp4)  # <------------------------------------------------------------------------

    # Build the expression tree from the tokenized mathematical expression.
    tree = ExpTreeBuilder.build_exp_tree(exp)

    # Traverse and evaluate the expression tree in order.
    value = Evaluator.evaluate_vars(tree, {'x': 1})
    print(value)

    graph_values = Grapher.x_interval(tree)
    plt.plot(graph_values[0], graph_values[1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("(x+((x+5)^2))")
    plt.show() #

if __name__ == "__main__":
    main()