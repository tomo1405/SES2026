python
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func():
    X = np.linspace(-10, 10, 400)
    Y = X**2

    plt.figure()
    plt.plot(X, Y)
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def test_task_func():
    task_func()
    assert plt.gcf().number == 1