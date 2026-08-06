import pytest
from src_0049 import task_func
import random
import time
from datetime import datetime
import matplotlib.pyplot as plt

def test_task_func():
    # Test with default parameters
    result = task_func(5)
    assert isinstance(result, list), "The result should be a list"
    assert len(result) == 5, "The length of the result should be 5"

    # Test with output path
    output_path = "test_output.png"
    result = task_func(5, output_path=output_path)
    assert os.path.exists(output_path), "The output file should be saved"
    os.remove(output_path)  # Clean up

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(-1)