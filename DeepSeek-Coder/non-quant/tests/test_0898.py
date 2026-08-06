import pytest
from src_0898 import task_func
import numpy as np
import matplotlib.pyplot as plt
import random

def test_task_func():
    # Test with seed for reproducibility
    seed = 42
    rolls = 1000
    expected_frequencies = [150, 150, 150, 150, 150, 150]

    frequencies, _ = task_func(rolls, seed=seed)

    assert np.array_equal(frequencies, expected_frequencies), "Frequencies do not match the expected frequencies."

    # Additional assertions to check the plot
    # This part is more complex as it requires checking the plot visually or programmatically
    # For simplicity, we assume the plot is correctly generated and saved.

if __name__ == "__main__":
    pytest.main()