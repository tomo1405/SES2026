import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
def task_func(func, x_range=(-2, 2), num_points=1000):
    X = np.linspace(x_range[0], x_range[1], num_points)
    y = func(X)
    y_int = integrate.cumulative_trapezoid(y, X, initial=0)

    fig, ax = plt.subplots()
    ax.plot(X, y, label=f"{func.__name__}(x)")
    ax.plot(X, y_int, label=f"Integral of {func.__name__}(x)")
    ax.legend()

    return ax