import math
import random

import numpy as np


def test_task_func():
    size = 1000
    frequency = 1
    x_values = np.arange(0, size)
    y_values = [math.sin((2 * np.pi / RANGE) * (x + int(RANGE * random.random()) * frequency)) for x in range(size)]
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values)
    
    assert ax.get_xlabel() == 'X'
    assert ax.get_ylabel() == 'Y'
    assert ax.get_title() == 'Sine Wave'
    assert ax.get_xlim() == (0, size)
    assert ax.get_ylim() == (-1, 1)
    assert ax.get_xticks() == np.arange(0, size, 100)
    assert ax.get_yticks() == np.arange(-1, 1, 0.1)
    assert ax.get_xticklabels() == ['0', '100', '200', '300', '400', '500', '600', '700', '800', '900']
    assert ax.get_yticklabels() == ['-1.0', '-0.9', '-0.8', '-0.7', '-0.6', '-0.5', '-0.4', '-0.3', '-0.2', '-0.1', '0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']