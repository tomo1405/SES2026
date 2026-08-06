import pytest
from src_0803 import task_func

def test_task_func_dimension_zero():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_dimension_negative():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_dimension_positive():
    matrix, flat_list = task_func(3)
    assert matrix.shape == (3, 3)
    assert len(flat_list) == 9

def test_task_func_reproducibility():
    matrix1, _ = task_func(3, seed=42)
    matrix2, _ = task_func(3, seed=42)
    assert np.array_equal(matrix1, matrix2)

def test_task_func_combinations():
    _, flat_list = task_func(3)
    combinations = list(itertools.combinations(flat_list, 2))
    assert len(combinations) == 36  # C(9, 2) = 36

def test_task_func_flat_list_length():
    _, flat_list = task_func(4)
    assert len(flat_list) == 16

def test_task_func_matrix_values():
    matrix, _ = task_func(2)
    assert np.all((matrix >= 1) & (matrix <= 100))

def test_task_func_flat_list_values():
    _, flat_list = task_func(2)
    assert all((value >= 1) and (value <= 100) for value in flat_list)