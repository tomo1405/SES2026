import matplotlib.pyplot as plt
import numpy as np


def test_task_func():
    X = np.linspace(-10, 10, 400)
    Y = X**2

    plt.figure()
    plt.plot(X, Y)
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

    assert plt.title() == 'y = x^2'
    assert plt.xlabel() == 'x'
    assert plt.ylabel() == 'y'
    assert plt.grid() == True
    assert plt.show() == True