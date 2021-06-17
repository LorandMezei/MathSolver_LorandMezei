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
    tk = Tokenizer()
    exp = tk.tokenize_math_exp(exp2)  #<--------------------------------------------------------------------------------

    # Build the expression tree from the tokenized mathematical expression.
    etb = ExpTreeBuilder()
    tree = etb.build_exp_tree(exp)

    # Traverse and evaluate the expression tree in order.
    ev = Evaluator()
    value = ev.evaluate_vars(tree, {'x': 1})
    print(value)

    #gr = Grapher()
    #graph_values = gr.x_1to10(tree, ev)
    #plt.plot(graph_values[0], graph_values[1])
    #plt.show()

if __name__ == "__main__":
    main()