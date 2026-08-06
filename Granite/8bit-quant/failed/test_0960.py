import pytest
from src_0960 import task_func
import string
import random

def test_task_func():
    # Test with a seed
    seed = 123
    random.seed(seed)
    text = "Hello, World!"
    expected_result = "Yberz vcfhz!"
    result = task_func(text, seed)
    assert result == expected_result, "Task function returned an incorrect result with a seed"

    # Test without a seed
    text = "Python is a great language!"
    expected_result = "Nevyhz thyfr vg'f nsg!"
    result = task_func(text)
    assert result == expected_result, "Task function returned an incorrect result without a seed"

if __name__ == "__main__":
    pytest.main()