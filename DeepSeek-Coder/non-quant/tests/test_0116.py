import pytest
from src_0116 import task_func
import numpy as np
from scipy.stats import mode
from scipy.stats import entropy

def test_task_func():
    # Test case 1: Normal case
    numbers = [1, 2, 2, 3, 3, 3]
    result = task_func(numbers)
    assert result['array'].tolist() == [1, 2, 2, 3, 3, 3]
    assert result['mode'] == 3
    assert pytest.approx(result['entropy'], 1.45914791718791)

    # Test case 2: Empty input
    with pytest.raises(ValueError):
        task_func([])

    # Add more test cases as needed