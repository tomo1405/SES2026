import pytest
from src_0279 import task_func

def test_task_func():
    # Test with default precision and seed
    solutions = task_func()
    assert len(solutions) == 2
    assert all(isinstance(solution, complex) for solution in solutions)
    assert all(solution.real >= -10 and solution.real <= 10 for solution in solutions)
    assert all(solution.imag >= -10 and solution.imag <= 10 for solution in solutions)

    # Test with custom precision and seed
    solutions = task_func(precision=3, seed=1234)
    assert len(solutions) == 2
    assert all(isinstance(solution, complex) for solution in solutions)
    assert all(solution.real >= -10 and solution.real <= 10 for solution in solutions)
    assert all(solution.imag >= -10 and solution.imag <= 10 for solution in solutions)

    # Test with invalid precision
    with pytest.raises(ValueError):
        task_func(precision=-1)

    # Test with invalid seed
    with pytest.raises(ValueError):
        task_func(seed=-1)