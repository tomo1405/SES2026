import pytest
from src_0279 import task_func
import numpy as np
from sympy import symbols, Eq, solve

def test_task_func():
    # Test with default parameters
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2
    for sol in result:
        assert isinstance(sol, complex)

    # Test with specific seed to ensure reproducibility
    result_seed_0 = task_func(seed=0)
    result_seed_0_expected = (0.36+0j), (-2.86+0j)
    assert result_seed_0 == result_seed_0_expected

    # Test with different precision
    result_precision_3 = task_func(precision=3, seed=0)
    result_precision_3_expected = (0.359+0j), (-2.858+0j)
    assert result_precision_3 == result_precision_3_expected

    # Test with negative seed
    result_negative_seed = task_func(seed=-1)
    assert isinstance(result_negative_seed, tuple)
    assert len(result_negative_seed) == 2
    for sol in result_negative_seed:
        assert isinstance(sol, complex)

    # Test with large seed
    result_large_seed = task_func(seed=123456789)
    assert isinstance(result_large_seed, tuple)
    assert len(result_large_seed) == 2
    for sol in result_large_seed:
        assert isinstance(sol, complex)

    # Test with zero coefficients (degenerate case)
    def mock_random_uniform(low, high):
        if low == -10 and high == 10:
            return 0
        else:
            return np.random.uniform(low, high)

    np.random.uniform = mock_random_uniform
    result_zero_coeffs = task_func(seed=0)
    result_zero_coeffs_expected = (0-0j), (0-0j)
    assert result_zero_coeffs == result_zero_coeffs_expected

    # Restore original np.random.uniform
    np.random.uniform = np.random.default_rng().uniform

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])