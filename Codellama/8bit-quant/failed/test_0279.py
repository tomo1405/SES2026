import pytest
from src_0279 import task_func

def test_task_func():
    # Test with default precision and seed
    solutions = task_func()
    assert len(solutions) == 2
    assert solutions[0] == complex(round(complex(solutions[0]).real, 2), round(complex(solutions[0]).imag, 2))
    assert solutions[1] == complex(round(complex(solutions[1]).real, 2), round(complex(solutions[1]).imag, 2))

    # Test with custom precision and seed
    solutions = task_func(precision=3, seed=1234)
    assert len(solutions) == 2
    assert solutions[0] == complex(round(complex(solutions[0]).real, 3), round(complex(solutions[0]).imag, 3))
    assert solutions[1] == complex(round(complex(solutions[1]).real, 3), round(complex(solutions[1]).imag, 3))

    # Test with invalid precision
    with pytest.raises(ValueError):
        task_func(precision=-1)

    # Test with invalid seed
    with pytest.raises(ValueError):
        task_func(seed=-1)