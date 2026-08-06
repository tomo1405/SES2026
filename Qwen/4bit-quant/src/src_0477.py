import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def task_func(X, Y):

    def func(x, a, b, c):
        return a * x ** 2 + b * x + c

    popt, pcov = curve_fit(func, X, Y)

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, func(X, *popt), "r-")

    return list(popt), ax