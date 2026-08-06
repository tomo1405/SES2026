import numpy as np
from sympy import symbols, solve
from src_0279 import task_func
import pytest

@pytest.mark.parametrize("precision, seed, expected_solutions", [
    (2, 0, (-2.0+0j, 1.0-1.73j, 1.0+1.73j)),
    (3, 1, (-2.000+0.000j, 1.000-1.732j, 1.000+1.732j)),
    (4, 2, (-2.0000+0.0000j, 1.0000-1.7321j, 1.0000+1.7321j)),
])
def test_task_func(precision, seed, expected_solutions):
    np.random.seed(seed)
    solutions = task_func(precision, seed)
    assert solutions == expected_solutions