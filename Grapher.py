import numpy as np


class Grapher():
    @staticmethod
    def x_interval(tree, ev):
        vars = {'x': 1}
        x = np.array([])
        y = np.array([])
        for i in range(1, 11):
            value = ev.evaluate_vars(tree, vars)
            x = np.append(x, i)
            y = np.append(y, value)
            vars['x'] += 1
        return [x, y]