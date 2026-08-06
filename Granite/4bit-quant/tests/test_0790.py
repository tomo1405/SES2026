import pytest
from src_0790 import task_func

def test_task_func():
    # Mock the numpy.random.seed() function to ensure reproducibility
    import numpy as np
    np.random.seed(42)

    # Call the function and store the result
    result = task_func()

    # Define the expected result
    expected_result = np.array([[0.52173913], [0.77124352], [0.48083333], [0.0473253 ], [0.89130435], [0.20447154], [0.1245283 ], [0.28441295], [0.79521276], [0.02594712]])

    # Assert that the result matches the expected result
    assert result.all() == expected_result.all()