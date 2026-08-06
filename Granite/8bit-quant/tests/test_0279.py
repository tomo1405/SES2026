import numpy as np
from sympy import symbols, solve
from src_0279 import task_func
import pytest

@pytest.mark.parametrize("precision, seed, expected_solutions", [
    (2, 0, ((-1.0, 0.0), (-0.66, -1.33), (-0.66, 1.33))),
    (3, 1, ((-1.0, 0.0), (-0.666, -1.333), (-0.666, 1.333))),
    (4, 2, ((-1.0, 0.0), (-0.6660, -1.3330), (-0.6660, 1.3330))),
])
def test_task_func(precision, seed, expected_solutions):
    np.random.seed(seed)
    solutions = task_func(precision, seed)
    assert solutions == expected_solutions