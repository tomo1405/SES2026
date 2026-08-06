import numpy as np
from sympy import symbols, solve
from src_0279 import task_func

def test_task_func():
    precision = 2
    seed = 0
    np.random.seed(seed)
    a = np.random.uniform(-10, 10)
    b = np.random.uniform(-10, 10)
    c = np.random.uniform(-10, 10)

    x = symbols('x')
    equation = a * x**2 + b * x + c

    solutions = solve(equation, x)
    expected_solutions = [complex(round(complex(solution).real, precision), round(complex(solution).imag, precision)) for solution in solutions]

    actual_solutions = task_func(precision, seed)

    assert actual_solutions == expected_solutions

def test_task_func_with_custom_precision_and_seed():
    precision = 3
    seed = 42
    np.random.seed(seed)
    a = np.random.uniform(-10, 10)
    b = np.random.uniform(-10, 10)
    c = np.random.uniform(-10, 10)

    x = symbols('x')
    equation = a * x**2 + b * x + c

    solutions = solve(equation, x)
    expected_solutions = [complex(round(complex(solution).real, precision), round(complex(solution).imag, precision)) for solution in solutions]

    actual_solutions = task_func(precision, seed)

    assert actual_solutions == expected_solutions