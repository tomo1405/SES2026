import pytest
from src_0279 import task_func

def test_task_func_with_seed():
    # Test with a fixed seed to ensure reproducibility
    seed = 42
    expected_solutions = ((-0.35+0j), (0.85+0j))
    assert task_func(precision=2, seed=seed) == expected_solutions

def test_task_func_with_different_precision():
    # Test with a different precision
    seed = 42
    expected_solutions = ((-0.351+0j), (0.851+0j))
    assert task_func(precision=3, seed=seed) == expected_solutions

def test_task_func_with_no_real_roots():
    # Test with a seed that results in no real roots
    seed = 100
    expected_solutions = ((-1.5+0.5j), (-1.5-0.5j))
    assert task_func(precision=1, seed=seed) == expected_solutions

def test_task_func_with_zero_coefficients():
    # Test with a seed that results in zero coefficients
    seed = 1
    expected_solutions = ((-0.05+0j), (-0.05+0j))
    assert task_func(precision=2, seed=seed) == expected_solutions

def test_task_func_with_large_coefficients():
    # Test with a seed that results in large coefficients
    seed = 200
    expected_solutions = ((-0.05+0j), (-0.05+0j))
    assert task_func(precision=2, seed=seed) == expected_solutions