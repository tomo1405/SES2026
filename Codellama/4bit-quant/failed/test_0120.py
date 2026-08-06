import pytest
from src_0120 import task_func

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

    assert plt.title.get_text() == 'y = x^2'
    assert plt.xlabel.get_text() == 'x'
    assert plt.ylabel.get_text() == 'y'
    assert plt.grid.get_visible() == True
    assert plt.show.get_visible() == True