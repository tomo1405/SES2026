import pytest
from src_0383 import task_func
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_length():
    length = 1000
    distribution, ax = task_func(length)
    assert len(distribution) == length

def test_task_func_distribution_mean():
    length = 1000
    distribution, _ = task_func(length)
    mean = np.mean(distribution)
    assert np.isclose(mean, 0, atol=0.1)

def test_task_func_distribution_std():
    length = 1000
    distribution, _ = task_func(length)
    std = np.std(distribution)
    assert np.isclose(std, 1, atol=0.1)

def test_task_func_plot():
    length = 1000
    _, ax = task_func(length)
    # Capture the plot to a buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Convert buffer to base64 string
    b64_data = base64.b64encode(buf.read()).decode('utf-8')
    # Check if the plot contains the expected elements
    assert 'Histogram' in ax.get_legend().get_texts()[0].get_text()
    assert 'PDF' in ax.get_legend().get_texts()[1].get_text()

# Run the tests
if __name__ == "__main__":
    pytest.main()