import numpy as np
from Evaluator import Evaluator


class Grapher():
    @staticmethod
    def x_interval(tree):
        vars = {'x': 1}
        x = np.array([])
        y = np.array([])
        for i in range(1, 101):
            value = Evaluator.evaluate_vars(tree, vars)
            x = np.append(x, i)
            y = np.append(y, value)
            vars['x'] += 1
        return [x, y]