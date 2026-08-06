import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from pytest import raises

def task_func(x):
    if not isinstance(x, np.ndarray):
        raise TypeError("x must be numpy.ndarray")

    real_part = norm.pdf(x, 0, 1)
    imag_part = norm.pdf(x, 2, 2)
    complex_dist = real_part + 1j * imag_part

    plt.plot(x, complex_dist.real, label='Real part')
    plt.plot(x, complex_dist.imag, label='Imaginary part')
    plt.legend()
    plt.grid()
    plt.show()
    return complex_dist

def test_task_func():
    x = np.linspace(-5, 5, 100)
    y = task_func(x)
    assert isinstance(y, np.ndarray)
    assert y.shape == (100,)
    assert np.all(np.iscomplex(y))
    with raises(TypeError):
        task_func([1, 2, 3])