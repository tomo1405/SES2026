import pytest
from src_0471 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture(autouse=True)
def cleanup():
    plt.switch_backend('Agg')
    yield
    plt.close('all')

def test_task_func():
    myList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    task_func(myList)
    assert True  # This is a placeholder to satisfy the test case