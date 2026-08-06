python
import numpy as np
import pytest
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    np.random.seed(seed)
    a = np.random.uniform(-10, 10)
    b = np.random.uniform(-10, 10)
    c = np.random.uniform(-10, 10)

    x = symbols('x')
    equation = a * x**2 + b * x + c

    solutions = solve(equation, x)
    solutions = [complex(round(complex(solution).real, precision), round(complex(solution).imag, precision)) for solution in solutions]

    return tuple(solutions)

def test_task_func():
    assert task_func() == (2.0+3.0j, -1.0+2.0j)
    assert task_func(precision=1) == (2.0+3.0j, -1.0+2.0j)
    assert task_func(precision=3) == (2.000+3.000j, -1.000+2.000j)
    assert task_func(seed=1) == (2.0+3.0j, -1.0+2.0j)
    assert task_func(precision=1, seed=1) == (2.0+3.0j, -1.0+2.0j)
    assert task_func(precision=3, seed=1) == (2.000+3.000j, -1.000+2.000j)