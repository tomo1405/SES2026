import pytest
from src_1064 import task_func
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture(scope="module")
def setup():
    plt.switch_backend('Agg')  # Avoids showing plots in test environment

def test_task_func(setup):
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    result = task_func(arr)
    assert result is not None
    plt.savefig('test_plot.png')
    plt.close()