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

    assert plt.gca().get_title() == 'y = x^2'
    assert plt.gca().get_xlabel() == 'x'
    assert plt.gca().get_ylabel() == 'y'
    assert plt.gca().get_grid() == True
    assert plt.gca().get_xlim() == (-10, 10)
    assert plt.gca().get_ylim() == (-100, 100)