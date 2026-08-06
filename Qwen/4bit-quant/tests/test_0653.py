import pytest
from src_0653 import task_func
import numpy as np
import matplotlib.pyplot as plt
import io
import sys

# Redirect stdout and stderr to suppress plot output during tests
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

@pytest.fixture
def no_plot():
    plt.switch_backend("Agg")

def test_task_func_with_default_target_value(no_plot):
    with Capturing() as output:
        result = task_func()
    assert result == ('N/A', 'N/A', 'N/A', 'N/A'), f"Expected ('N/A', 'N/A', 'N/A', 'N/A'), got {result}"

def test_task_func_with_custom_target_value(no_plot):
    custom_array = np.array([['332', '1', '2'], ['332', 'bb', 'ccc'], ['332', '33', '2'], ['33', '22', '332']])
    with Capturing() as output:
        result = task_func(target_value='332', array=custom_array)
    assert result == (1.5, 0.25, 0.0, -1.2), f"Expected (1.5, 0.25, 0.0, -1.2), got {result}"

def test_task_func_with_insufficient_data(no_plot):
    small_array = np.array([['332', '1', '2']])
    with Capturing() as output:
        result = task_func(array=small_array)
    assert result == ('N/A', 'N/A', 'N/A', 'N/A'), f"Expected ('N/A', 'N/A', 'N/A', 'N/A'), got {result}"