import numpy as np
from Evaluator import Evaluator


class Grapher():
    @staticmethod
    def x_interval(tree, x_start, x_end):
        vars = {'x': x_start}
        x = np.array([])
        y = np.array([])
        for i in range(x_start, x_end):
            value = Evaluator.evaluate_vars(tree, vars)
            x = np.append(x, i)
            y = np.append(y, value)
            vars['x'] += 1
        return [x, y]